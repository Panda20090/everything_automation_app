import pandas as pd
import json  # Add this line

def analyze_google_trends_data(file_path):
    df = pd.read_csv(file_path)
    # Example analysis: calculate average value
    avg_value = df['normalized_value'].mean()
    insights = {
        "average_value": avg_value,
        "total_entries": len(df)
    }
    with open('data/google_trends_insights.json', 'w') as f:
        json.dump(insights, f)
    return insights

def analyze_twitter_data(file_path):
    df = pd.read_csv(file_path)
    # Example analysis: count tweets containing certain keywords
    keyword_count = df['text'].str.contains('AI').sum()
    insights = {
        "keyword_count": keyword_count,
        "total_tweets": len(df)
    }
    with open('data/twitter_insights.json', 'w') as f:
        json.dump(insights, f)
    return insights
