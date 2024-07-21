import requests
import json

def track_metrics():
    url = 'https://api.mockmetrics.com/v1/metrics'
    response = requests.get(url)
    metrics = response.json()
    with open('data/performance_metrics.json', 'w') as f:
        json.dump(metrics, f)
    return metrics

def analyze_feedback(feedback_file):
    with open(feedback_file, 'r') as f:
        feedback = json.load(f)
    # Example analysis
    positive_feedback = [item for item in feedback if item['rating'] >= 4]
    negative_feedback = [item for item in feedback if item['rating'] < 4]
    analysis = {
        'positive': positive_feedback,
        'negative': negative_feedback
    }
    with open('data/feedback_analysis.json', 'w') as f:
        json.dump(analysis, f)
    return analysis
