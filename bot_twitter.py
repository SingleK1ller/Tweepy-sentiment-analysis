import tweepy
from textblob import TextBlob as tb
import matplotlib.pyplot as plt
import os

tokens_path = os.path.join(os.path.dirname(__file__), "keys.txt")
with open(tokens_path, "r") as f:
    tokens = f.readlines()

bearer_token = tokens[0].strip()
consumer_key = tokens[1].strip()
consumer_secret = tokens[2].strip()
access_token = tokens[3].strip()
access_token_secret = tokens[4].strip()

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

def analyze_sentiment(text):
    analysis = tb(text)
    return analysis.sentiment.polarity

def generate_plot(polarities, x_axis):
    plt.title("Sentiment Polarity")
    plt.plot(x_axis, polarities, marker='o', linestyle='-')
    plt.xlabel("Tweets")
    plt.ylabel("Polarity")
    plt.savefig("sentiment_plot.png")

# Replace with your way to obtain tweets
tweets = ["This is a positive tweet.", "This is a negative tweet."]

polarities = [analyze_sentiment(tweet) for tweet in tweets]
x_axis = range(len(tweets))

generate_plot(polarities, x_axis)

media_id = client.media_upload(filename="sentiment_plot.png")

tweet_text = "Análise de sentimento dos tweets: #python #nlp"
client.create_tweet(text=tweet_text, media_ids=[media_id])
