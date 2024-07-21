import pandas as pd

def process_google_trends_data(file_path):
    data = pd.read_json(file_path)
    # Example processing: Extracting required information and creating a DataFrame
    trends = data.get('trends', [])
    df = pd.DataFrame(trends)
    df.to_csv('data/processed_google_trends_data.csv', index=False)
    return df

def process_twitter_data(file_path):
    data = pd.read_json(file_path)
    # Example processing: Extracting tweet texts and creating a DataFrame
    tweets = data.get('data', [])
    df = pd.DataFrame(tweets)
    df.to_csv('data/processed_twitter_data.csv', index=False)
    return df
