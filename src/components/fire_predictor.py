import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.exception import MyException
from src.logger import logging
from src.data_access.fire_data import FireDataFetcher


class FirePredictor:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise MyException(e, sys)

    async def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Initiating data ingestion...")
            fire_data_fetcher = FireDataFetcher()
            await fire_data_fetcher.init_config(source="VIIRS_SNPP_NRT", data_engestion_config=self.data_ingestion_config)

            logging.info("Fetching data from NASA API...")
            # Using defaults or config values for country/state if needed, but FireDataFetcher calls nasa_db which uses yaml.
            # However, export_collection_as_dataframe takes country, stateArgs.
            # We should probably pass them from config or use defaults.
            # Assuming "india" and "karnataka" as per previous context or config.
            # The config_entity doesn't have country/state yet, but I added them in the plan?
            # Wait, I proposed adding them to ConfigEntity but I only added paths in step 55.
            # I should use hardcoded values or update config.
            # Let's use hardcoded "india", "karnataka" for now as per previous code snippets or assume 
            # we need to pass them.
            
            dataframe = await fire_data_fetcher.export_collection_as_dataframe(
                country=self.data_ingestion_config.country, 
                state=self.data_ingestion_config.state, 
                day_range=self.data_ingestion_config.day_range
            )
            
            logging.info(f"Data fetched successfully. Shape: {dataframe.shape}")

            feature_store_path = self.data_ingestion_config.feature_store_file_path
            
            # The FireDataFetcher already saved the raw file to feature_store_file_path (via nasa_db).
            # But here we got the dataframe.
            
            logging.info("Performing train_test_split")
            train_set, test_set = train_test_split(
                dataframe, 
                test_size=self.data_ingestion_config.train_test_split_ratio
            )

            logging.info("Saving train and test files")
            os.makedirs(os.path.dirname(self.data_ingestion_config.training_file_path), exist_ok=True)
            
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path,
                feature_store_path=feature_store_path
            )
            
            logging.info(f"Data ingestion completed. Artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise MyException(e, sys)
