import pandas as pd

def analyze_google_trends_data(file_path):
    df = pd.read_csv(file_path)
    # Example analysis
    insights = df.describe()
    insights.to_json('data/google_trends_insights.json')
    return insights

def analyze_twitter_data(file_path):
    df = pd.read_csv(file_path)
    # Example analysis
    insights = df['text'].value_counts()
    insights.to_json('data/twitter_insights.json')
    return insights
