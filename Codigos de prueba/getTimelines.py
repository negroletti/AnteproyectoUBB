#TODO: Search for specific tweets with query
import json
import tweepy
import re

consumer_key = "jRzLpZOlvCOLoLhdIz4JiTp1W"
consumer_secret = "vIkH0Ta3ENYonsrKFwTZyaiQWzuf6AmKsbsoL3CGDhl3uaEXGp"
access_token = "826036108404412419-2Py0qpB93VkCLFt6HyYRaxz6PuvzQ6P"
access_secret = "3rJOgr7O5pQb2PqXaUfFaYPwK09qtxuT0Sb95DwidoCJJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

x=[]
def getTimelines():
    for tweet in tweepy.Cursor(api.user_timeline, screen_name="aguirreseba",tweet_mode="extended", include_rts=False).items(5):
        print(json.dumps(tweet._json, indent=4))
        #x.append(json.dumps(tweet._json, indent=4))
        #f_out = open("tweets.json", "w")
        #for i in x:
            #json.dump(i, f_out)
            #f_out.write(",")
            #f_out.write("\n")

if __name__ == '__main__':
    getTimelines()