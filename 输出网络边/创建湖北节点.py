# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/2/1 14:13'
import pandas as pd
city_name=['咸宁市', '随州市', '仙桃市', '黄石市', '神农架林区', '荆门市', '潜江市', '孝感市', '鄂州市', '荆州市', '恩施土家族苗族自治州', '十堰市', '黄冈市', '襄阳市', '天门市', '武汉市', '宜昌市']

city_latlng=[[29.841199638680287,114.32200002765934],[31.69030058523121,113.38299957624614]
             ,[30.327808562443895,113.4430708646698],[30.19939960293492,115.03900003418904]
             ,[31.74460031047552,110.67599978780419],[31.03539989309376,112.20000022843752]
             ,[30.40220042749318,112.89899997927145],[30.92480004292067,113.91599992196133]
             ,[30.390900497976883,114.89499986501862],[30.335000380826443,112.23899990797712]
             ,[30.272200939196907,109.4879997112762],[32.62920058688821,110.79800000487187]
             ,[30.45339975507176,114.87200001362683],[32.00900052477173,112.12199980021491],
             [30.663299439124792,113.1660004274518],[30.592799572064738,114.30500043085405],[30.691700466222986,111.28599985191957]]
lat=[]
lng=[]
for i in city_latlng:
    lat.append(i[0])
    lng.append(i[1])
data = {'name':city_name,'lat':lat,'lng':lng}
df_data = pd.DataFrame(data, index=None)

df_data.to_csv('hubeipoint.csv', index=None, encoding="utf_8_sig")