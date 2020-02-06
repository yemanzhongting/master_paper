# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/1/31 19:52'
import json,time
import pandas as pd
from urllib.request import urlopen, quote
import re
from 坐标纠偏 import bd09togcj02,gcj02towgs84
def getlnglat(address):
    #http://api.map.baidu.com/geocoder/v2/?address=北京市海淀区上地十街10号&output=json&ak=您的ak&callback=showLocation //GET请求
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = '8399wyuCP00HcW0c7rHfjMpCIT6dA4mC' # 浏览器端密钥
    address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak
    print(uri)
    req = urlopen(uri,timeout=6)
    res = req.read().decode()
    temp = json.loads(res)
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']

    code=temp['status']
   # print(lat, lng,code,)
    return lat, lng

def bdtowgs84(lng,lat):
    tmp=bd09togcj02(lng,lat)
    return gcj02towgs84([tmp[0],tmp[1]])

latlng=('武汉市')
geocode=getlnglat(latlng)
t_geocode=bd09togcj02(geocode[1],geocode[0])
print(t_geocode)

with open('输出去重.txt','r+',encoding='utf-8') as f:
    tmp=f.readlines()
f.close()
#with open('输出去重带纠偏经纬度.txt','w+',encoding='utf-8') as f:

area = []
code = []
lat = []
lng = []
for i in tmp:
    latlng=i.split(',')[0]
    print(i)
    print(latlng)
    area.append(latlng)
    t_code=(i.split(',')[1]).replace('\n','')

    code.append(t_code)
    try:
        #round(a/b,2)
        geocode=getlnglat(latlng)#获取地点，格式lat ,lng
        t_geocode=bd09togcj02(geocode[1],geocode[0])#lng,lat
        print(t_geocode)
        #exam.append(i)
        lat.append(t_geocode[1])#lat
        lng.append(t_geocode[0])#lng

        time.sleep(0.2)
    except:
        #exam.append(i)
        lat.append('')
        lng.append('')
        time.sleep(0.2)
print(area)
print(code)
print(lat)
print(lng)

data = {'area':area,
        'code': code,
        'lat':lat,
        'lng':lng}
df = pd.DataFrame(data,index=None)


#df = pd.DataFrame([area,code,lat,lng], columns=['area','code','lat','lng'])
df.to_csv('输出去重带纠偏经纬度.csv',encoding="utf_8_sig",index=None)

