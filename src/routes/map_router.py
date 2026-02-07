import fastapi
from src.pipeline.data_fetcher_pipeline import Data_Fetcher_Pipeline
from src.exception import MyException
from src.logger import logging
from src.utils.main_utils import delete_folders
router=fastapi.APIRouter()
import os
import sys

@router.post("/")
async def map_locations(
    country: str = "india",
    state: str = "up",
    day_range: int = 3
):
    try:
        delete_folders()
        pipeline=Data_Fetcher_Pipeline(country=country,state=state,day_range=day_range)
        data_ingestion_artifact=await pipeline.start_data_ingestion()
        data_transformation_artifact=await pipeline.start_data_transformation(data_ingestion_artifact)

        html=None
        with open(data_transformation_artifact.map_file_path,"r") as f:
            html=f.read()
        return {"html": html}
    except Exception as e:
        logging.error(f"Error in map_locations: {str(e)}")
        raise MyException(e, sys)
    