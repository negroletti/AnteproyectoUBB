from nltk.sentiment.vader import SentimentIntensityAnalyzer

x= "Good evening for everyone, I'm happy"
print(type(x))
sid = SentimentIntensityAnalyzer()
resultados = sid.polarity_scores(x)

print(resultados)