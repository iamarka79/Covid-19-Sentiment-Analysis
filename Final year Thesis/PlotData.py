# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 01:08:52 2020

@author: Arka
"""

import numpy as np
from matplotlib import pyplot as plt
import csv

date = []
covid_Economy_pos = []
covid_Economy_neg = []
sum_pos = 0
sum_neg = 0
count_pos = 0
count_neg = 0
with open('Output.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        date.append(str(row[0]))
        covid_Economy_pos.append(row[7])
        covid_Economy_neg.append(row[8])

plt.plot(date,covid_Economy_pos,covid_Economy_neg, label='Sentiment over Covid Economy')
plt.xlabel('date')
plt.ylabel('positive sentiment over covid Economy')
#plt.ylabel('negative sentiment over covid Economy')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()