import tweepy

def twitter():
    auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAAGYlAEAAAAATZEjgAfyIt9bzgsIDM7Iy1GD%2BJs%3DgxBaThvZR4x9AhCRRiHJzkQVdOaB06sAgHm6aceBdm0RDNUujd")

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)