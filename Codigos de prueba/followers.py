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
x=[];

def searchFollowers():
    for  user in tweepy.Cursor(api.friends, screen_name="ccmvaldivia").items(100):
        x.append(user._json['screen_name'])
    print (x)
    f_out = open("Valdivia3.txt", "w")
    for i in x:
        f_out.write(i + "\n")

        


if __name__ == "__main__":
    searchFollowers()