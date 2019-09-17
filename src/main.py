import tweepy
import configparser
import pandas as pd
from loguru import logger


def write_tweet(tweet, file):
    line = f'{tweet.id},{tweet.user.screen_name},{tweet.user.location}\n'
    file.write(line)

file = open('data.txt', 'a')

config = configparser.ConfigParser()
config.read('credentials.ini')

auth = tweepy.OAuthHandler(config['DEFAULT']['consumer_key'],config['DEFAULT']['consumer_secret'])
auth.set_access_token(config['DEFAULT']['access_token'],config['DEFAULT']['access_token_secret'])

search_words = "#python"

api = tweepy.API(auth)
tweets = tweepy.Cursor(api.search,
                        q = search_words,
                        lang = 'en',
                        ).items()

# users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
#
# tweet_texts = pd.DataFrame(data=users_locs,
#                     columns=['user', "location"])

n = 0

for tweet in tweets:
    write_tweet(tweet, file)

file.close()
