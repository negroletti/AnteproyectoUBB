import json
import carmen
import tweepy
import re

consumer_key = "jRzLpZOlvCOLoLhdIz4JiTp1W"
consumer_secret = "vIkH0Ta3ENYonsrKFwTZyaiQWzuf6AmKsbsoL3CGDhl3uaEXGp"
access_token = "826036108404412419-2Py0qpB93VkCLFt6HyYRaxz6PuvzQ6P"
access_secret = "3rJOgr7O5pQb2PqXaUfFaYPwK09qtxuT0Sb95DwidoCJJ"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

searchTerms = "#Wallmart"
noOfSearch = 1
searchCountry = "USA"

places = api.geo_search(query=searchCountry, granularity="country")
place_id = places[0].id

tweets = tweepy.Cursor(api.search , q=(searchTerms) and ("place:%s" % place_id), lang="English").items(noOfSearch)

for tweet in tweets:
    print(tweet.text + "| " + tweet.place.name if tweet.place else "Undefined place")