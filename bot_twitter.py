import tweepy
from textblob import TextBlob as tb
import matplotlib.pyplot as plt


def showGraph(polarities, subjectivity, xAxis):
    plt.title("Polarity")
    plt.plot(xAxis, polarities, '-', color='red')
    plt.plot(xAxis, subjectivity, '-', color='blue')
    plt.show()
"""
consumer_key = 'key q tenho q colocar'
consumer_secret = 'segredinho rsrs'
access_token = 'token de acesso'
access_token_secret = 'secret token acesso'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

"""
#public_tweets = api.search(q='python', count=100)
public_tweets = ["Fuck you", "I hate you", "Sorry"]


xAxis = range(len(public_tweets))

polarities = []
subject = []
for tweet in public_tweets:
    analysis = tb(tweet)
    polarities.append(analysis.sentiment.polarity)
    subject.append(analysis.sentiment[1])

showGraph(polarities, subject, xAxis)
average_polarity = sum(polarities) / len(polarities)
print("Média de sentimento: ", average_polarity)



