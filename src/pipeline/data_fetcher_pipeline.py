import sys
import os
import asyncio

# Add project root to sys.path
sys.path.append(os.getcwd())
from dotenv import load_dotenv
load_dotenv()

from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.components.data_transformation import DataTransformation
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataTransformationArtifact
from src.entity.config_entity import DataValidationConfig, ModelTrainerConfig
from src.logger import logging
from src.exception import MyException


class Data_Fetcher_Pipeline:
    def __init__(self, country: str = "india",
    state: str = "up",
    source: str = "VIIRS_SNPP_NRT",
    day_range: int = 3):
        self.data_ingestion_config = DataIngestionConfig(country=country,state=state,day_range=day_range)
        self.data_validation_config = DataValidationConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        # self.model_evaluation_config = ModelEvaluationConfig()
        # self.model_pusher_config = ModelPusherConfig()


    
    async def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=await data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e, sys) from e

    # async def start_data_validation(self,data_ingestion_artifact: DataIngestionArtifact)->DataValidationArtifact:
    #     try:
    #         logging.info("Entered the start_data_validation method of TrainPipeline class")
    #         logging.info("Validating The Data")
    #         data_validation =DataValidation()
    #         await data_validation.init_config(data_validation_config=self.data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
    #         data_validation_artifact=await data_validation.initiate_data_validation()
    #         logging.info("Data Validation Completed")
    #         logging.info("Exited the start_data_validation method of TrainPipeline class")
    #         return data_validation_artifact
    #     except Exception as e:
    #         raise MyException(e, sys) from e
        
    async def start_data_transformation(self,data_ingestion_artifact:DataIngestionArtifact)->DataTransformationArtifact:
        try:
            logging.info("Entererd the start_data_transformation method of TrainingPipeline Class")
            logging.info("transforming the data")
            
            data_transformation=DataTransformation(data_transformation_config=self.data_transformation_config)
            data_transformation_artifact=await data_transformation.initiate_data_transformation(data_ingestion_artifact=data_ingestion_artifact)
            
            return data_transformation_artifact
        except Exception as e:
            raise MyException(e,sys)
        

    