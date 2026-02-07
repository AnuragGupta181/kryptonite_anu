import sys
import os

sys.path.append(os.getcwd())
try:
    from from_root import from_root
    print(f"from_root imported successfully. Root: {from_root()}")
    
    from src.logger import logging
    print("logger imported successfully.")
    
    from src.components.data_ingestion import DataIngestion
    print("DataIngestion imported successfully.")
    
except Exception as e:
    print(f"Import failed: {e}")
