import requests
import json
import os

def retrieve_google_trends_data(api_key, keyword):
    url = f"https://www.googleapis.com/trends/v1beta1/data?key={api_key}&keyword={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open('data/google_trends_data.json', 'w') as f:
            json.dump(data, f)
        return data
    else:
        raise ValueError("Failed to retrieve data from Google Trends API")

def retrieve_twitter_data(api_key, query):
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&tweet.fields=created_at&expansions=author_id"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        with open('data/twitter_data.json', 'w') as f:
            json.dump(data, f)
        return data
    else:
        raise ValueError("Failed to retrieve data from Twitter API")
