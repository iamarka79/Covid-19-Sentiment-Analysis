# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 22:58:06 2020

@author: Supriyo
"""

import nltk
import unicodedata
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
   # print(words)
    p=nltk.pos_tag(words)
    #print(p)
    Output = [item for item in p if  item[1] == 'NNS' or item[1]=='NNP' or item[1]=='NN' or item[1]=='NNPS' or item[1]=='JJ' or item[1]=='JJR' or item[1]=='JJS' or item[1]=='RB' or item[1]=='RBR' or item[1]=='RBS' or item[1]=='VB' or item[1]=='VBD' or item[1]=='VBN' or item[1]=='VBP' or item[1]=='VBG' or item[1]=='VBZ']
   # print(Output)
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
       
   # print(list1)
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
    return pos,neg
                  
                
# Main function                                
s="05-05-20.txt"
pos,neg=sentiscore(s)
print(pos)
print(neg)    