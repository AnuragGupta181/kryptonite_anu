import os
import sys
import pandas as pd
import folium

from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataIngestionArtifact,DataTransformationArtifact
from src.exception import MyException
from src.logger import logging
from src.constants import COLORS
from src.constants import copy_js
from branca.element import Element





class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig):
        try:
            self.data_transformation_config = data_transformation_config
        except Exception as e:
            raise MyException(e, sys)

    async def initiate_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataTransformationArtifact:
        try:
            logging.info("Starting data transformation")
            data = pd.read_csv(data_ingestion_artifact.feature_store_path)
            colors = COLORS
            center_lat = data["latitude"].mean()
            center_lon = data["longitude"].mean()



            m = folium.Map(location=[center_lat, center_lon], zoom_start=6, tiles="Esri.WorldImagery")
            m.get_root().html.add_child(Element(copy_js))


            for _, row in data.iterrows():
                popup_html = f"""
                Date: {row['acq_date']}, Time: {row['acq_time']}<br>
                Lat: {row['latitude']}, Lon: {row['longitude']}<br>
                <button onclick="copyCoords({row['latitude']}, {row['longitude']})">
                Copy Coordinates
                </button>
                """
                folium.CircleMarker(
                    location=[row["latitude"], row["longitude"]],
                    radius=4,
                    color=colors.get(row["confidence"], "yellow"),
                    fill=True,
                    fill_opacity=0.7,
                    popup=popup_html
                ).add_to(m)


            os.makedirs(os.path.dirname(self.data_transformation_config.map_file_path), exist_ok=True)
            logging.info(f"Data transformation artifact created: {self.data_transformation_config.map_file_path}")
            file_name = self.data_transformation_config.map_file_path
            m.save(file_name)
            logging.info("Data transformation completed")
            logging.info(f"Data transformation artifact created: {self.data_transformation_config.map_file_path}")

            return DataTransformationArtifact(
                map_file_path=file_name,
                train_file_path=data_ingestion_artifact.train_file_path,
                test_file_path=data_ingestion_artifact.test_file_path,
                feature_store_path=data_ingestion_artifact.feature_store_path
            )
        except Exception as e:
            raise MyException(e, sys)
