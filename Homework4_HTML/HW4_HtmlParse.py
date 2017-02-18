from bs4 import BeautifulSoup
import urllib
from watson_developer_cloud import AlchemyLanguageV1

import json
from os.path import join, dirname

in_file = open(".apikey", "r")
watson_api_key = in_file.read().splitlines()
in_file.close()


alchemy_language = AlchemyLanguageV1(api_key=watson_api_key)
link = "https://twitter.com/realDonaldTrump"
f = urllib.urlopen(link)
website = f.read()

soup =  BeautifulSoup(website)
tweets =  soup('p', {'class': 'tweet-text'})

print ( "Sentiment of the last 20 texts from Donald Trump @theRealDonaldTrump")

for tweet in tweets:
    print "Tweet Text " + tweet.contents[0]
    response = alchemy_language.sentiment(text=tweet.contents[0], language='english', )
    print "Sentiment: " + response["docSentiment"]["type"]
    print ""


