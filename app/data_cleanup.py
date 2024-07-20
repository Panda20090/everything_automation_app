import pandas as pd

def clean_google_trends_data(file_path):
    df = pd.read_csv(file_path)
    # Example cleanup: remove NaN values, normalize data, etc.
    df.dropna(inplace=True)
    df['normalized_value'] = (df['value'] - df['value'].min()) / (df['value'].max() - df['value'].min())
    df.to_csv('data/cleaned_google_trends_data.csv', index=False)
    return df

def clean_twitter_data(file_path):
    df = pd.read_csv(file_path)
    # Example cleanup: remove NaN values, filter out irrelevant data, etc.
    df.dropna(subset=['text'], inplace=True)
    df = df[df['text'].str.contains('AI')]
    df.to_csv('data/cleaned_twitter_data.csv', index=False)
    return df
