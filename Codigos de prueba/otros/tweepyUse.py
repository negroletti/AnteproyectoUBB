
#Obtener datos de mi usuario
#data = api.me()
#print (json.dumps(data._json, indent=2))

#Obtener datos de otro usuario por su username
#data = api.get_user("nike")
#print (json.dumps(data._json, indent=2))

#Obtener Followers de un usuario con Cursor usando metodo api.followers
#for  user in tweepy.Cursor(api.followers, screen_name="nike").items(100):
#   print(json.dumps(user._json, indent=2))

#Obtener folowees/friends de un usuario
#for  user in tweepy.Cursor(api.friends, screen_name="nike").items(2):
#    print(json.dumps(user._json, indent=2))

#Obtener un timeline
#for tweet in tweepy.Cursor(api.user_timeline, screen_name="nike",tweet_mode="extended").items(1):
#    print(json.dumps(tweet._json, indent=2))
