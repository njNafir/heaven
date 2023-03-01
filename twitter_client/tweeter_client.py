
import tweepy
from dotenv import load_dotenv
import os
from websocket import create_connection
import json

load_dotenv()

ws = create_connection(os.environ["WEBSOCKET_SERVER_URL"])

auth = tweepy.OAuthHandler(os.environ["TWITTER_API_KEY"], os.environ["TWITTER_API_SECRET_KEY"])
auth.set_access_token(os.environ["TWITTER_ACCESS_TOKEN"],
                      os.environ["TWITTER_ACCESS_TOKEN_SECRET"])
api = tweepy.API(auth)

class TwitterListener(tweepy.StreamListener):
  def on_status(self, status):
    ws.send(json.dumps(status._json))
    print(status._json)

twitterListener = TwitterListener()
myStream = tweepy.Stream(auth=api.auth, listener=twitterListener)
myStream.filter(track=['javascript', 'nodejs', 'python'])