# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:37:11 2020

@author: Arka
"""
import csv




#main

txt = 'West Bengal has recorded 15 deaths due to COVID-19 in the past 48 hours, noted official bulletin of the State Health department released late on Saturday evening.Two bulletins — one for May 1 and another for May 2 — was released by the Health Department. While seven persons had died between May 1 and May 2, eight deaths were recorded between April 30 and May 1. In the past two days, 127 new viral infections were recorded and 60 persons were discharged from the hospitals in the State.After a gap of 48 hours, the COVID -19 bulletin of State Health Department had a different format. Cumulative total number of persons expired due to COVID-19 and cumulative total Number of active COVID-19 cases are two the inputs which were published till April 30 and has now been removed from the bulletin.Till April 30 the number of people who had died after getting infected was 105. The State government maintained that 33 of the patients died of COVID-19, and 72 others died of "co-morbidities" where COVID-19 was "incidental finding".With 15 more deaths, the number of people who died after getting infected by the virus in the State has increased to 120, with 72 "co-morbidities." The bulletin also added that there are 16 sample testing labs in the State and 2,410 samples were tested in the past 24 hours. The State has tested over 20,976 samples so far.'
txt = txt.lower()
#print(txt)
with open('Case1.csv','rt') as f:
    data = csv.reader(f)
    for row in data:
        l = len(row)
        count = 0
        for i in range(l):
            if row[i] in txt:
                count += 1
print(count, ' ', count/l)