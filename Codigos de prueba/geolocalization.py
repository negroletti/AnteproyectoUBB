#Geolocalization of the user Twitter
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

def searchTweets():
    print("searching for tweets: ")
    #Buscar Tweets
    for tweet in tweepy.Cursor(api.search, q="#CuartoRetiro",tweet_mode="extended").items(100000):
        if((tweet._json["user"]["location"]) != None):
            data = tweet._json["user"]["location"]
            text = tweet._json["full_text"]
            print(data)
            print(filter(text))         

def filter(data):
    if(data.find("RT")!=-1):
        data = data.replace('RT:','')
        data = re.sub(r'^\W*\w+\W*','',data)
    else:
        data= re.sub(r'^\W*\w+\W*','',data)
    data = deEmojify(data)
    data = deURL(data)
    return data

#Quitar Emojis
def deEmojify(data):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',data)

#Quitar URLs
def deURL(data):
    data = re.sub(r'http\S+', '', data)
    return data

if __name__ == '__main__':
    searchTweets()