import pandas as pd

def clean_google_trends_data(file_path):
    df = pd.read_csv(file_path)
    # Example cleaning: Remove rows with missing values
    df = df.dropna()
    df.to_csv('data/cleaned_google_trends_data.csv', index=False)
    return df

def clean_twitter_data(file_path):
    df = pd.read_csv(file_path)
    # Example cleaning: Remove rows with missing values
    df = df.dropna()
    df.to_csv('data/cleaned_twitter_data.csv', index=False)
    return df
