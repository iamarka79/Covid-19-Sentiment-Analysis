# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:40:25 2020

@author: Arka
"""

#from lxml import html
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image
#import PIL.Image
#from pytesseract import image_to_string
import pytesseract
from textblob import TextBlob
import nltk
from newspaper import Article
#import urllib3 as urllib
#import io

page = requests.get('https://epaper.telegraphindia.com/imageview_323261_154849937_4_71_11-03-2020_15_i_1_sf.html')

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='mergeimg')
#print(results.prettify)
images = results.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')
    url = image['src']
    image = Image.open(requests.get(url, stream=True).raw)
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    #fd = requests.get(image['src'])
    #image_file = io.BytesIO(fd.content)
    #im = Image.open(image_file)
    #image = Image.open(im)
    image_to_text = pytesseract.image_to_string(image, lang='eng')
    print(image_to_text)
    obj = TextBlob(image_to_text)
    sentiment = obj.sentiment.polarity
    print("Sentiment Value : ",sentiment)
    print()