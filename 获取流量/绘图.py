# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/1/31 22:22'
#cmap(颜色)

import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns
import pandas as pd

df=pd.read_csv(r'hubei.csv', engine='python', sep=',',
                         encoding="utf_8_sig")
# print(df)
#
# df2=df[2:]
# print(df2)

data=df.values[:,2:32].astype(int)

height = 17
width = 30

print(data)

plt.matshow(data, cmap='hot')
plt.colorbar()
plt.show()