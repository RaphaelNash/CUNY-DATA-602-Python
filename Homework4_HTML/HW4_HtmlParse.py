from bs4 import BeautifulSoup
import urllib
from watson_developer_cloud import AlchemyLanguageV1
import json
from os.path import join, dirname


""" This program fetches a news article from Yahoo! News, passes the text to the
AlchemyLanuage API and retrieve the top 10 keywords by relevence:

"""

full_text = ""

in_file = open(".apikey", "r")
watson_api_key = in_file.read().splitlines()
in_file.close()

alchemy_language = AlchemyLanguageV1(api_key=watson_api_key)
link = "https://www.yahoo.com/news/advances-imaging-could-deepen-knowledge-brain-200758111.html"
website = urllib.urlopen(link).read()

soup =  BeautifulSoup(website, "html.parser")
article =  soup('p', {'class': 'canvas-atom'})

for paragraph in article:
    full_text = full_text + '\n' + paragraph.contents[0]

response = alchemy_language.keywords(text=full_text,  max_keywords=10, )

keywords = response["keywords"]

print "Top 10 keywords from the article: "+ link + ":"
print("key word:relevence")
print("------------------")
for word in keywords:
    print word["text"] +":" + word["relevance"]

