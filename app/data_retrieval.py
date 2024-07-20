import requests
import json

def retrieve_google_trends_data(api_key, keyword):
    url = f"https://www.googleapis.com/trends/v1beta1/data?key={api_key}&keyword={keyword}"
    response = requests.get(url)
    data = response.json()
    with open('data/google_trends_data.json', 'w') as f:
        json.dump(data, f)
    return data

def retrieve_twitter_data(api_key, query):
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&tweet.fields=created_at&expansions=author_id"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    with open('data/twitter_data.json', 'w') as f:
        json.dump(data, f)
    return data
