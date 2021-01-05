# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 03:25:41 2020

@author: Arka
"""
import csv
from matplotlib import pyplot as plt
count = 0
sum_pos = 0
sum_neg = 0
li = []
li_neg = []
week = []
with open('Output.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        count += 1
        sum_pos += float(row[7])
        sum_neg += float(row[8])
        if count == 7:
            count = 0
            li.append(sum_pos)
            li_neg.append(sum_neg)
            sum_pos = 0
            sum_neg = 0
li.append(sum_pos)
li_neg.append(sum_neg)
for i in range(len(li)):
    week.append(i+1)

plt.plot(week,li,label='Positive sentiment over Covid Public Health Awareness')
plt.xlabel('week')
plt.ylabel('sentiment over covid PHA')
#plt.ylabel('negative sentiment over covid Education')
plt.plot(week,li_neg,label='Negative sentiment over Covid Public Health Awareness')
plt.xlabel('week')
plt.ylabel('sentiment over covid PHA')
plt.title('Covid Graph Plot')
plt.legend()
#plt.savefig('Covid_PHA_Weekwise.pdf')
plt.savefig('plot.png', bbox_inches='tight')
plt.show()