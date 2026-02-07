import sys
import pandas as pd
import numpy as np
from typing import Optional
import logging
from src.configuration.nasa_db_connection import Nasa_fire_db
from src.constants import DATABASE_NAME_KEY
from src.exception import MyException
from src.entity.config_entity import DataIngestionConfig
from src.configuration.nasa_db_connection import Nasa_fire_db
import pandas as pd
class FireDataFetcher:
    def __init__(self):
        pass
    async def init_config(self,source:str,data_engestion_config:DataIngestionConfig):
        try:
            self.nasa_db=Nasa_fire_db()
            await self.nasa_db.init_config(source=source,data_engestion_config=data_engestion_config)

        except Exception as e:
            raise MyException(e,sys)


    async def export_collection_as_dataframe(self,country:str,state:str,day_range:int)->pd.DataFrame:
        try:
            logging.info("Connecting to database")
            feature_store_file_path = await self.nasa_db.export_collection_as_dataframe(country=country, state=state, day_range=day_range)
            df = pd.read_csv(feature_store_file_path)

            return df
        except Exception as e:
            raise MyException(e,sys)
    
        



         

            