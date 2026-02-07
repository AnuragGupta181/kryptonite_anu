import fastapi
from fastapi import UploadFile
import shutil
import base64
router=fastapi.APIRouter()
import os
import pandas as pd
import requests
# from dotenv import load_dotenv
# import geopandas
# import folium
from ultralytics import YOLO
from pathlib import Path




model = YOLO("saved_model/fire_detector.pt")

async def draw_boxes(image_path, save_dir="outputs"):
    results = model(
        image_path,
        conf=0.25,
        save=True,
        project=save_dir,
        name="fires",
    )

    r = results[0]
    save_path = Path(r.save_dir)

    images = list(save_path.glob("*.jpg")) + list(save_path.glob("*.png"))
    if not images:
        raise FileNotFoundError("YOLO output image not found")

    return str(images[0])
@router.post("/draw_boxes_fire")
async def draw_yolo_boxes(file: UploadFile):
    os.makedirs("public", exist_ok=True)

    if not file:
        return JSONResponse(status_code=400, content={"error": "File is required"})

    file_path = f"public/{file.filename}"

    # save uploaded file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # run YOLO inference
    output_image_path = await draw_boxes(image_path=file_path)

    # read output image
    with open(output_image_path, "rb") as f:
        image_bytes = f.read()

    # cleanup
    os.remove(file_path)
    shutil.rmtree(os.path.dirname(output_image_path), ignore_errors=True)

    encoded_image = base64.b64encode(image_bytes).decode("utf-8")
    save_path = f"public/saved_{file.filename}"  # e.g., public/saved_input.jpg
    with open(save_path, "wb") as f:
        f.write(base64.b64decode(encoded_image))
    return {"data": encoded_image}