import re

def deUrl(text):
    text= re.sub(r'http\S+', '', text)
    return text

text= "text1, text2"
print(deUrl(text))