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
x = set()
y = set()
z = set()

def searchFollowers():
    for  user in tweepy.Cursor(api.friends, screen_name="UTalca").items(100):
        x.add(user._json['screen_name'])
    print ("1 listo")
    f_out = open("Talca1.txt", "w")
    for i in x:
        f_out.write(i + "\n")
    for user in tweepy.Cursor(api.friends, screen_name="RADIOPALOMAFM").items(100):
        y.add(user._json['screen_name'])
    print ("2 listo")
    f_out = open("Talca2.txt", "w")
    for i in y:
        f_out.write(i + "\n")
    for user in tweepy.Cursor(api.friends, screen_name="IMTalca").items(100):
        z.add(user._json['screen_name'])
    print ("3 listo")
    f_out = open("Talca3.txt", "w")
    for i in z:
        f_out.write(i + "\n")

    j= x.intersection(y)
    print(j)
    k= j.intersection(z)
    print(k)

    f_out = open("TalcaF.txt", "w")
    for i in k:
        f_out.write(i + "\n")


if __name__ == "__main__":
    searchFollowers()