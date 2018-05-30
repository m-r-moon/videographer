###############################
# Filename: tweet.py          #
# Author: Mitchel R Moon      #
###############################

import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

api.update_status('status')
