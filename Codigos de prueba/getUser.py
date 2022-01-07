import json
import tweepy
import re

consumer_key = "jRzLpZOlvCOLoLhdIz4JiTp1W"
consumer_secret = "vIkH0Ta3ENYonsrKFwTZyaiQWzuf6AmKsbsoL3CGDhl3uaEXGp"
access_token = "826036108404412419-2Py0qpB93VkCLFt6HyYRaxz6PuvzQ6P"
access_secret = "3rJOgr7O5pQb2PqXaUfFaYPwK09qtxuT0Sb95DwidoCJJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

def getTwitterUser():
    api = tweepy.API(auth)
    user = api.get_user('luisnunezcatala')
    print(json.dumps(user._json, indent=4))
    #print(json.dumps(user._json['screen_name'], indent=2))
    #print(json.dumps(user._json['location'], indent=2))
    #print(json.dumps(user._json['status']['place'], indent=2))
    #print(json.dumps(user._json['status']['geo'], indent=2))
    #print(json.dumps(user._json['status']['coordinates'], indent=2))


if __name__ == '__main__':
    getTwitterUser()