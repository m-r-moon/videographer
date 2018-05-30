#!/usr/bin/python

import argparse
import tweepy
from time import sleep
from credentials import *

def tweet(filename, status, video):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)
  api = tweepy.API(auth)

  api.update_with_media(filename, status, video)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('totalLength', help='Specify total length (s, m, h)')
  parser.add_argument('frequency', help='Specify photo frequency (s, m, h)')
  parser.add_argument('project', help='Specify project name')
  args = parser.parse_args()

  if args.totalLength and args.frequency and args.project:
    print 'start taking photos...'
    # start taking photos

    # compile photos

    # tweet video
    tweet(filename, status, video)
  else:
    print parser.usage
    exit(0)

if __name__ == '__main__':
  main()
