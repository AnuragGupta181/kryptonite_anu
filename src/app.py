from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()
from src.routes.home_router import router as HomeRouter
from src.routes.map_router import router as MapRouter
app=FastAPI(title="Fire Detector",description="Kryptonite hackathon")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(HomeRouter,prefix="/api/user")
app.include_router(MapRouter,prefix="/api/map")
