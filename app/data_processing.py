import pandas as pd
import os

def process_google_trends_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    
    with open(file_path, 'r') as f:
        data = f.read()
    
    if data.strip() == "":
        raise ValueError("No data to process.")
    
    return pd.read_json(file_path)

def process_twitter_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    
    with open(file_path, 'r') as f:
        data = f.read()
    
    if data.strip() == "":
        raise ValueError("No data to process.")
    
    return pd.read_json(file_path)
