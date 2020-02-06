# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/1/31 20:10'
from 获取医院坐标.坐标纠偏 import bd09togcj02,gcj02towgs84
import json,time
import pandas as pd
from urllib.request import urlopen, quote

def getlnglat(address):
    # http://api.map.baidu.com/geocoder/v2/?address=北京市海淀区上地十街10号&output=json&ak=您的ak&callback=showLocation //GET请求
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = '8399wyuCP00HcW0c7rHfjMpCIT6dA4mC'  # 浏览器端密钥
    address = quote(address)  # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    print(uri)
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']

    code = temp['status']
    # print(lat, lng,code,)
    return lat, lng

def bdtowgs84(lng,lat):
    tmp=bd09togcj02(lng,lat)
    return gcj02towgs84([tmp[0],tmp[1]])

def get_file():
    data = pd.read_csv('武汉市医院.csv', engine='python', sep=',', encoding="utf_8_sig")
    print(data.head())
    list = data['医院名称'].values.tolist()
    print(list)
    data['lat'] = None
    data['lng'] = None
    for i in list:
        # print(i)
        try:
            geocode = getlnglat(i)
            t_geocode = bd09togcj02(geocode[1], geocode[0])
            time.sleep(1)

            print([t_geocode[1], t_geocode[0]])
            data.loc[list.index(i), 'lat'] = t_geocode[1]
            data.loc[list.index(i), 'lng'] = t_geocode[0]
        except:
            print('error')
            print(i)
    print(data)
    data.to_csv('result_arcgis.csv', index=None, encoding="utf_8_sig")

if __name__ == '__main__':
    t_geocode = bd09togcj02(114.373403,30.527368)
    print(t_geocode)

    # latlng=('火神山医院')
    # geocode=getlnglat(latlng)
    # t_geocode=bd09togcj02(geocode[1],geocode[0])
    # print([t_geocode[1],t_geocode[0]])