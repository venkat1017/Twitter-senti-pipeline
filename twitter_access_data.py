###Importing necessary module for json formatter
import json

##using twitter sdk to download twitter data

from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

###Adding twitter consumer key and secret access tokens

consumer_key = 'SYQj4TA2p6Ofz5EPJ9WcYw'
consumer_secret = 'M7KkzgIWkUm29WiXwRSxBjMMipijFnHXKWlNa4gDE'
access_token ='945680196-pQSNsACaksk4nOp61k3y5sL85AQEGqq70C8HfOxs'
access_token_secret ='Ivw35mJ0OlZtWOtZ0vmBi3ineWe9lyGqUjjvhujXqqY0S'



###Set authentication using OAuthHandler
auth = OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                  status.created_at,
                  status.source,
                  '\n')

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True # keep stream alive

    def on_timeout(self):
        print('Listener timed out!')
        return True # keep stream alive


def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)


def pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))


if __name__ == '__main__':
    # print_to_terminal()
    pull_down_tweets(auth.username)