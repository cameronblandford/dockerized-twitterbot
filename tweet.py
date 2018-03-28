#! /usr/bin/env python

from random import randint
import tweepy
import secrets

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)

    api = tweepy.API(auth)
    api.update_status("Hello World! ({})".format(randint(0,1000)))
