# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#from textblob import TextBlob
from textblob import TextBlob
import nltk
from newspaper import Article
url = 'https://www.telegraphindia.com/india/jyotiraditya-delivers-holi-shock-for-congress/cid/1752528?ref=top-stories_home-template'
article = Article(url)
article.download()
article.parse()
nltk.download('punkt')
article.nlp()
print(article)
text = article.summary
print(text)
obj = TextBlob(text)
sentiment = obj.sentiment.polarity
print("Sentiment Value : ",sentiment)
print(article.keywords)
if(sentiment == 0):
    print('This text is neutral')
elif(sentiment > 0):
    print('This text is postive')
else:
    print('This text is negative')