import fastapi
router=fastapi.APIRouter()
from src.pipeline.data_fetcher_pipeline import Data_Fetcher_Pipeline
from src.exception import MyException
import pandas as pd
import json
from src.utils.main_utils import delete_folders

import sys
import logging
@router.post("/get_hight_regions_area")
async def high_regions(
    country: str = "india",
    state: str = "up",
    day_range: int = 3
):
    try:
            delete_folders()
            pipeline=Data_Fetcher_Pipeline(country=country,state=state,day_range=day_range)
            data_ingestion_artifact=await pipeline.start_data_ingestion()
            data_transformation_artifact=await pipeline.start_data_transformation(data_ingestion_artifact)

            data=pd.read_csv(data_transformation_artifact.feature_store_path)
            data=data[data['confidence']=='h']
            data=json.dumps(data.to_dict())
            
            return {"data": data}
   
    except Exception as e:
        logging.error(f"Error in map_locations: {str(e)}")
        raise MyException(e, sys)