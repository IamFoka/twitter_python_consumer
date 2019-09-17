import tweepy
import configparser
import pandas as pd
from loguru import logger

config = configparser.ConfigParser()
config.read('credentials.ini')

auth = tweepy.OAuthHandler(config['DEFAULT']['consumer_key'],config['DEFAULT']['consumer_secret'])
auth.set_access_token(config['DEFAULT']['access_token'],config['DEFAULT']['access_token_secret'])

search_words = "#marvel"

api = tweepy.API(auth)
tweets = tweepy.Cursor(api.search,
                        q = search_words,
                        lang = 'pt',
                        ).items()

# users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
#
# tweet_texts = pd.DataFrame(data=users_locs,
#                     columns=['user', "location"])

n = 0

for tweet in tweets:
    logger.info(n)
    logger.info(tweet.created_at)
    n += 1
