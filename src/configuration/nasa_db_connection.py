import os
import pandas as pd
import requests
from dotenv import load_dotenv
import geopandas
import folium
from ultralytics import YOLO
from pathlib import Path
from src.exception import MyException
from src.utils.main_utils import read_yaml_file
from src.constants import REGION_BOX_YAML_PATH,BASE_URL,MAP_KEY,TRAIN_FILE_NAME
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
import logging
import requests
import sys


class Nasa_fire_db:
    def __init__(self):
        pass
    async def init_config(self,source:str,data_engestion_config:DataIngestionConfig):
        logging.info("connected to the Nasa fire db")
        self.source=source
        self.region_box=await read_yaml_file(REGION_BOX_YAML_PATH)
        self.MAP_KEY=os.getenv(MAP_KEY)
        self.data_ingestion_config=data_engestion_config

    async def export_collection_as_dataframe(self,country:str,state:str,day_range:int)->DataIngestionArtifact:
            try:
                country=country.lower()
                state=state.lower()
                if country not in self.region_box or state not in self.region_box[country]:
                     logging.debug(f"country or state not found in {self.region_box}")
                     raise Exception(f"country or state not found in {self.region_box}")
    
                area=self.region_box[country][state]
                url = f"{BASE_URL}/api/area/csv/{self.MAP_KEY}/{self.source}/{area}/{day_range}"
                response=requests.get(url, timeout=30)
    
                if response.status_code != 200:
                    raise ConnectionError(response.text)
                
                dir_path = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
                os.makedirs(dir_path, exist_ok=True)

                with open(self.data_ingestion_config.feature_store_file_path, "wb") as f:
                        f.write(response.content)

                return self.data_ingestion_config.feature_store_file_path
            
            except Exception as e:
                 raise MyException(e,sys)
    
    
         
    
