import requests

def publish_to_medium(title, content, access_token):
    url = "https://api.medium.com/v1/users/{userId}/posts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "title": title,
        "contentFormat": "html",
        "content": content,
        "publishStatus": "public"
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def publish_to_wordpress(title, content, url, username, password):
    from wordpress_xmlrpc import Client, WordPressPost
    from wordpress_xmlrpc.methods.posts import NewPost

    client = Client(url, username, password)
    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = 'publish'
    post_id = client.call(NewPost(post))
    return post_id

def publish_to_twitter(content, api_key, api_secret_key, access_token, access_token_secret):
    import tweepy

    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)
    status = api.update_status(content)
    return status.id
