# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 03:26:41 2020

@author: Arka
"""

import datetime
import pandas as pd

#print(datetime.datetime.today().strftime('%d-%m-%Y'))

start_date = '07-01-2020'
end_date = datetime.datetime.today()
daterange = pd.date_range(start_date, end_date)

for ele in daterange:
    single_date = ele.strftime('%d-%m-%Y')
    print(str(single_date))
    