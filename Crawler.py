from bs4 import BeautifulSoup
import requests
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
import json
import _json

import TwitterCredentials

#class StandoutListener(StreamListener):
    #def on_data(self,data):
       # print(data)
       # return True

    #def on_error(self, status):
      #  pass


url="https://twitter.com/realDonaldTrump"

def get_twitter_auth():
    consumer_key=TwitterCredentials.API_KEY
    consumer_secret=TwitterCredentials.API_SECRET_KEY
    access_token=TwitterCredentials.ACCESS_TOKEN
    access_token_secret=TwitterCredentials.ACCESS_TOKEN_SECRET
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    return auth


def get_twitter_client():
    auth=get_twitter_auth()
    client=API(auth)
    return client

if __name__ =='__main__':
    user="realDonaldTrump"
    Myclient=get_twitter_client()

    with open('Trump_timeline.jsonl','w') as f:
        for status in Cursor(Myclient.user_timeline,screen_name=user).items(10):
            print(status.text)
            print("-------------------------------")
            f.write(json.dumps(status._json) + "\n")


