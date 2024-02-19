import tweepy
from textblob import TextBlob as tb

"""
consumer_key = 'key q tenho q colocar'
consumer_secret = 'segredinho rsrs'
access_token = 'token de acesso'
access_token_secret = 'secret token acesso'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

"""
public_tweets = api.search(q='python', count=100)

polarities = []
for tweet in public_tweets:
    analysis = tb(tweet.text)
    polarities.append(analysis.sentiment.polarity)

average_polarity = sum(polarities) / len(polarities)
print("Média de sentimento: ", average_polarity)



