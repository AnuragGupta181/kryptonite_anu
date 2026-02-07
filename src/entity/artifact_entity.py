from dataclasses import dataclass
from typing import Optional

@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str
    feature_store_path:str

@dataclass
class DataTransformationArtifact:
    map_file_path:str
    train_file_path:str
    test_file_path:str
    feature_store_path:str
