import requests
import json
import tweepy

def retrieve_google_trends_data(api_key, keyword):
    url = f"https://trends.googleapis.com/trends/v1beta1/data?api_key={api_key}&keyword={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        with open('data/google_trends_data.json', 'w') as f:
            json.dump(response.json(), f)
        return 'data/google_trends_data.json'
    else:
        response.raise_for_status()


def retrieve_twitter_data(api_key, api_secret_key, access_token, access_token_secret, keyword):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    tweets = api.search_tweets(q=keyword, lang='en', count=100)
    tweet_data = [{'text': tweet.text, 'created_at': tweet.created_at} for tweet in tweets]
    
    with open('data/twitter_data.json', 'w') as f:
        json.dump(tweet_data, f)
    
    return 'data/twitter_data.json'