# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/2/6 14:22'
import pandas as pd
import matplotlib.pyplot as plt
google=pd.read_csv('GOOGL_2006-01-01_to_2018-01-01.csv',index_col='Date', parse_dates=['Date'])
print(google.head())

#填补缺失
# humidity = humidity.iloc[1:]
# humidity = humidity.fillna(method='ffill')
# humidity.head()

timestamp = pd.Timestamp(2017, 1, 1, 12)
timestamp

google['2008':'2010'].plot(subplots=True, figsize=(10,12))
plt.title('Google stock attributes from 2008 to 2010')
plt.savefig('stocks.png')
plt.show()