# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:05:48 2020

@author: Arka
"""

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from PIL import Image
import pytesseract
import pandas as pd
#import io
import csv
#from textblob import TextBlob
import nltk


def news_select_covid_Economy(text):
    text = text.lower()
    with open('Covid_Economy.csv','rt') as f:
        data = csv.reader(f)
        for row in data:
            l = len(row)
            count = 0
            for i in range(l):
                if row[i] in text:
                    count += 1
    #print(count/l)
    return count/l


def news_select_Covid_Education(text):
    text = text.lower()
    with open('Covid_Education.csv','rt') as f:
        data = csv.reader(f)
        for row in data:
            l = len(row)
            count = 0
            for i in range(l):
                if row[i] in text:
                    count += 1
    #print(count/l)
    return count/l


def news_select_Covid_PHA(text):
    text = text.lower()
    with open('Covid_Public_Health_Awareness.csv','rt') as f:
        data = csv.reader(f)
        for row in data:
            l = len(row)
            count = 0
            for i in range(l):
                if row[i] in text:
                    count += 1
    #print(count/l)
    return count/l


def news_select_covid_death(text):
    text = text.lower()
    with open('Covid_Death.csv','rt') as f:
        data = csv.reader(f)
        for row in data:
            l = len(row)
            count = 0
            for i in range(l):
                if row[i] in text:
                    count += 1
    #print(count/l)
    return count/l



def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString  
def sentiscore(s):
    f = open(s,'r' ,encoding='utf8', errors='ignore')
    line = f.read()
    tokens = nltk.word_tokenize(line)
    words = [word for word in tokens if word.isalpha()]
    #print(words)
    p=nltk.pos_tag(words)
    #print(p)
    Output = [item for item in p if  item[1] == 'NNS' or item[1]=='NNP' or item[1]=='NN' or item[1]=='NNPS' or item[1]=='JJ' or item[1]=='JJR' or item[1]=='JJS' or item[1]=='RB' or item[1]=='RBR' or item[1]=='RBS' or item[1]=='VB' or item[1]=='VBD' or item[1]=='VBN' or item[1]=='VBP' or item[1]=='VBG' or item[1]=='VBZ']
    #print(Output)
    x = open("senti.txt" )
    s1=x.read()
    s = replaceMultiple(s1,['#1','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13','#14','#15'] , '')       
    x.close()
    x=open("senti.txt","w")
    x.write(s)
    x.close()
    list1=[]
    p=open('senti.txt')
    line=p.readline()
    while line:
        tokens = nltk.word_tokenize(line)
        slice_object = slice(5)
        q=tokens[slice_object]
        list1.append(q)
        line = p.readline()
    #print("******************************************************************")
       
    #print(list1)
    p.close()
    d=[]
    for j in Output:
        p=list(j)
        if p[1] in ['NNP','NNS','NN','NNPS']:
            p[1]='n'
        if p[1] in ['JJ','JJR','JJS']:
            p[1]='a'
        if p[1] in ['RB','RBR','RBS']:
            p[1]='r'
        if p[1] in ['VB','VBD','VBN','VBP','VBG','VBZ']:
            p[1]='v'
        d.append(tuple(p))
    #print(d)
    l=len(d)
    l1=len(list1)
    pos=0
    neg=0
    for i in d:
        q=list(i)
        for j in range(l1):
            if q[0]==list1[j][4]:
                pos=pos+float(list1[j][2])
                neg=neg+float(list1[j][3])
    pos=pos/l
    neg=neg/l
    #print(pos,' ',neg)
    return pos,neg



def fileWrite(start_date,article_count,senti_pos,senti_neg,d,li):
    f = open('Death_Metric.csv','a')
    f.write(start_date)
    f.write('\t')
    f.write(str(article_count))
    f.write('\t')
    print(start_date)
    print(d)
    print()
    #print(li)
    for ele in li:
        f.write(str(d[ele]))
        f.write('\t')
    f.write(str(senti_pos))
    f.write('\t')
    f.write(str(senti_neg))
    f.write('\n')
    return






def newsfeedProcessing(start_date,end_date):
    #start_date = '06-20-2020'
    #end_date = datetime.today()
    #end_date = '06-20-2020'
    li_main = ['covid 19','covid-19','death','co-morbidities','comorbidities','death rate','coronavirus','dead','die','died','hospital']
    d = dict()
    daterange = pd.date_range(start_date,end_date)
    for ele in daterange:
        single_date = ele.strftime('%Y-%m-%d')
        every_date = ele.strftime('%d-%m-%Y')
        page_no = 1
        #d = dict()
        for key in li_main:
            d[key] = 0
        url = 'https://epaper.telegraphindia.com/calcutta/'+ single_date +'/71/Page-'+ str(page_no) +'.html'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        total_pages = soup.find('input', {'id': 'totalpages'}).get('value')
        article_count1 = 0
        senti_pos1 = 0
        senti_neg1 = 0
        '''article_count2 = 0
        senti_pos2 = 0
        senti_neg2 = 0
        article_count3 = 0
        senti_pos3 = 0
        senti_neg3 = 0
        article_count4 = 0
        senti_pos4 = 0
        senti_neg4 = 0'''
        while(page_no <= int(total_pages)):
            url = 'https://epaper.telegraphindia.com/calcutta/'+ single_date +'/71/Page-'+ str(page_no) +'.html'
            #print(url)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(id='mainepaer')
            list = []
            images = results.find_all('area', attrs={'href':re.compile('#')})
            for image in images:
                li = []
                list = image.get('onclick').split()
                if list[1][0] == 's' and list[1][8] == 'h':
                    li = list[1][13:len(list[1])-1].split(',')
                    id1 = li[0]
                    id1 = id1[1:len(id1)-1]
                    id2 = li[1]
                    id2 = id2[1:len(id2)-1]
                    id3 = li[2]
                    id3 = id3[1:len(id3)-1]
                    string_url = 'https://epaper.telegraphindia.com/imageview_' + id1 +'_'+ id2 +'_'+ id3 +'_71_' + datetime.strftime(datetime.now(), '%d-%m-%Y') +'_'+str(page_no)+'_i_1_sf.html'
                    #print(string_url)
                    page = requests.get(string_url)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    results = soup.find(id='mergeimg')
                    images = results.find_all('img', {'src':re.compile('.jpg')})
                    for image in images: 
                        try:
                            url = image['src']
                            image = Image.open(requests.get(url, stream=True).raw)
                            pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
                            image_to_text = pytesseract.image_to_string(image, lang='eng')
                            val1 = news_select_covid_death(image_to_text)
                            val1 = float("{:.2f}".format(val1))
                            '''val2 = news_select_covid_Economy(image_to_text)
                            val2 = float("{:.2f}".format(val2))
                            val3 = news_select_Covid_Education(image_to_text)
                            val3 = float("{:.2f}".format(val3))
                            val4 = news_select_Covid_PHA(image_to_text)
                            val4 = float("{:.2f}".format(val4))'''
                            #print(val1)
                            if val1 >= 0.33:
                                text = image_to_text.lower().strip()
                                new_text = ''
                                text.replace('\n','')
                                text.replace('-\n','')
                                for line in text.split('\n'):
                                    stripped_line = line.rstrip()
                                    if len(new_text) > 0 and new_text[-1] == '-':
                                        new_text = new_text[:-1] + stripped_line
                                    else:
                                        new_text = new_text + ' ' + stripped_line
                                #print(new_text)
                                #print()
                                for k in text.split():
                                    #print('k = ',k)
                                    if k in d:
                                        #print('k = ',k)
                                        d[k] += 1
                                article_count1 += 1
                                f = open("05-05-20.txt","w")
                                f.write(new_text)
                                s = "05-05-20.txt"
                                pos,neg = sentiscore(s)
                                #print(article_count1,' ',pos,' ',neg)
                                senti_pos1 += pos
                                senti_neg1 += neg
                                f.close()
                                #flag = True
                            '''if val2 >= 0.16:
                                #print('Inside condition')
                                article_count2 += 1
                                #print(image_to_text)
                                #break
                                f = open("05-05-20.txt","w")
                                f.write(image_to_text)
                                s = "05-05-20.txt"
                                #obj = TextBlob(image_to_text)
                                #sentiment = obj.sentiment.polarity
                                #sentiment = float("{:.2f}".format(sentiment))
                                #print(article_count,' ',sentiment)
                                pos,neg = sentiscore(s)
                                #print(article_count1,' ',pos,' ',neg)
                                senti_pos2 += pos
                                senti_neg2 += neg
                                f.close()
                            if val3 >= 0.33:
                                #print('Inside condition')
                                article_count3 += 1
                                #print(image_to_text)
                                #break
                                f = open("05-05-20.txt","w")
                                f.write(image_to_text)
                                s = "05-05-20.txt"
                                #obj = TextBlob(image_to_text)
                                #sentiment = obj.sentiment.polarity
                                #sentiment = float("{:.2f}".format(sentiment))
                                #print(article_count,' ',sentiment)
                                pos,neg = sentiscore(s)
                                #print(article_count1,' ',pos,' ',neg)
                                senti_pos3 += pos
                                senti_neg3 += neg
                                f.close()
                            if val4 >= 0.33:
                                #print('Inside condition')
                                article_count4 += 1
                                #print(image_to_text)
                                #break
                                f = open("05-05-20.txt","w")
                                f.write(image_to_text)
                                s = "05-05-20.txt"
                                #obj = TextBlob(image_to_text)
                                #sentiment = obj.sentiment.polarity
                                #sentiment = float("{:.2f}".format(sentiment))
                                #print(article_count,' ',sentiment)
                                pos,neg = sentiscore(s)
                                #print(article_count1,' ',pos,' ',neg)
                                senti_pos4 += pos
                                senti_neg4 += neg
                                f.close()'''
                        except:
                            continue
            #if flag == True:
            #    break
            #print(d)
            page_no += 1

        if article_count1 > 0:
            senti_pos1 = senti_pos1/article_count1
            senti_neg1 = senti_neg1/article_count1
            #senti_pos1 = float("{:.4f}".format(senti_pos1))
            #senti_neg1 = float("{:.4f}".format(senti_neg1))
            senti_pos1 = format(senti_pos1,'.4f')
            senti_neg1 = format(senti_neg1,'.4f')
        else:
            senti_pos1 = 0.0000
            senti_neg1 = 0.0000
            senti_pos1 = format(senti_pos1,'.4f')
            senti_neg1 = format(senti_neg1,'.4f')
        print(senti_pos1,' ',senti_neg1)
        fileWrite(str(every_date),article_count1,senti_pos1,senti_neg1,d,li_main)
        #for ele in li:
         #   print(ele, ' = ', d[ele])



#main
start_date = '06-25-2020'
#end_date = datetime.today()
end_date = '06-30-2020'
newsfeedProcessing(start_date, end_date)