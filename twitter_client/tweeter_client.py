
import tweepy
from dotenv import load_dotenv
import os
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET_KEY"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"),
                      os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

class TwitterListener(tweepy.StreamListener):
  def on_status(self, status):
    print(status.text)

twitterListener = TwitterListener()
myStream = tweepy.Stream(auth=api.auth, listener=twitterListener)
myStream.filter(track=['javascript', 'nodejs', 'python'])