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
async def main():
    try:
        config = DataIngestionConfig()
        data_ingestion = DataIngestion(config)
        artifact = await data_ingestion.initiate_data_ingestion()
        
        data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation(data_transformation_config)
        data_transformation_artifact=await data_transformation.initiate_data_transformation(artifact)
        print(f"Data transformation artifact created: {data_transformation_artifact}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
