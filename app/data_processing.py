import pandas as pd
import os

def process_google_trends_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")
    data = pd.read_json(file_path)
    trends = data.get('trends', [])
    df = pd.DataFrame(trends)
    df.to_csv('data/processed_google_trends_data.csv', index=False)
    return df

def process_twitter_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")
    data = pd.read_json(file_path)
    tweets = data.get('data', [])
    df = pd.DataFrame(tweets)
    df.to_csv('data/processed_twitter_data.csv', index=False)
    return df
