import sys
import os
import asyncio

# Add project root to sys.path
sys.path.append(os.getcwd())
from dotenv import load_dotenv
load_dotenv()

from src.pipeline.data_fetcher_pipeline import Data_Fetcher_Pipeline

async def main():
    try:
        # Test with UP state
        print("Testing pipeline with country='india' and state='up'")
        pipeline = Data_Fetcher_Pipeline(country="india", state="up", day_range=3)
        
        print("Starting data ingestion...")
        data_ingestion_artifact = await pipeline.start_data_ingestion()
        print(f"Data ingestion artifact: {data_ingestion_artifact}")
        
        print("Starting data transformation...")
        data_transformation_artifact = await pipeline.start_data_transformation(data_ingestion_artifact)
        print(f"Data transformation artifact: {data_transformation_artifact}")
        
        if os.path.exists(data_transformation_artifact.map_file_path):
            print("Map file exists.")
            with open(data_transformation_artifact.map_file_path, 'r') as f:
                content = f.read()
                print(f"Map file content length: {len(content)}")
        else:
            print("Map file does NOT exist.")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
