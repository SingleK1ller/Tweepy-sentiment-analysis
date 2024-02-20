import tweepy
import requests
from textblob import TextBlob as tb
import matplotlib.pyplot as plt


bearer_token = 'AAAAAAAAAAAAAAAAAAAAAL7NsQEAAAAAtm62c5x8bI1Mrc0oHuCr2Z5C3Pw%3DMipCUX0LSppU2w5XQPhHrn3bnIFa2GJ4OKrW0ZDtqCzChKyaRm'
client = tweepy.Client(bearer_token=bearer_token, 
                       consumer_key='YBDraw0XQjcV4wNpYS8F5d2bs', 
                       consumer_secret='RqraaaqBealjE1iV8s1MUY8ciPyU1njfbEb4HvXHmiYLNt0N2C',
                       access_token='1759704638197039105-4AJDaU3HLPjKHbFfm4N2oSm3tSIkml',
                       access_token_secret='OT9GHXOw7inrS9RWrInpHiPKbZ3AbplGAaQbry9Pm9Hhb'
                       )

#tweets = [tweet['text'] for tweet in response_data['data']]

tweets = ["hi, i love you", "heyy i miss you"]
xAxis = range(len(tweets))

polarities = []
for tweet_text in tweets:
    analysis = tb(tweet_text)
    polarities.append(analysis.sentiment.polarity)

consumer_key = 'YBDraw0XQjcV4wNpYS8F5d2bs'
consumer_secret = 'RqraaaqBealjE1iV8s1MUY8ciPyU1njfbEb4HvXHmiYLNt0N2C'
access_token = '1759704638197039105-4AJDaU3HLPjKHbFfm4N2oSm3tSIkml'
access_token_secret = 'OT9GHXOw7inrS9RWrInpHiPKbZ3AbplGAaQbry9Pm9Hhb'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

average_polarity = sum(polarities) / len(polarities)
client.create_tweet(text="test")
