from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

def analyze_file_sentiment(file_path):
    df = pd.read_csv(file_path)
    df['Sentiment'] = df['text'].apply(analyze_sentiment)
    output_file = 'data/sentiment_analysis.csv'
    df.to_csv(output_file, index=False)
    return output_file
