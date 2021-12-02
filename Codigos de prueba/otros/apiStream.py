import tweepy

consumer_key = "jRzLpZOlvCOLoLhdIz4JiTp1W"
consumer_secret = "vIkH0Ta3ENYonsrKFwTZyaiQWzuf6AmKsbsoL3CGDhl3uaEXGp"
access_token = "826036108404412419-2Py0qpB93VkCLFt6HyYRaxz6PuvzQ6P"
access_secret = "3rJOgr7O5pQb2PqXaUfFaYPwK09qtxuT0Sb95DwidoCJJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        print(status.text)
    def on_error(self,status_code):
        if status_code == 420:
            return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['Educación'], is_async=True)