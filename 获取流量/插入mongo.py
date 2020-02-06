# -*- coding: UTF-8 -*-
import time

__author__ = 'zy'
__time__ = '2020/1/31 20:23'
import requests,re,json
url='http://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id={id}&type=move_out&startDate=20200101&endDate=20200130'
def write_con(tmp_url):
    global ip_random
    #ip_rand, proxies = get_proxie(ip_random)
    #print(proxies)
    #t=random.choice(proxies)
    #print(t)#proxies=t,
    result = requests.get(tmp_url, timeout=(3, 7))
    # try:

    # tmp=json.loads(json.dumps(result))
    # tmp=json.loads(result).get('cb')
    # js=result.json()
    # json1 = json.dumps(json.loads(result))
    pat = '"list":(.*?)}}\)'
    # pat1 = '{"city_name":".*?","province_name":".*?","value":(.*?)}'

    results = re.compile(pat).findall(str(result.content.decode("utf-8")).encode("utf-8").decode("unicode_escape"))

    print(results[0])
    temp = json.loads(results[0])

    return temp
    # for k, v in d.items():
    #     print(k, '=', v)

    # temp = json.loads(results[0])
    # for key,value in temp.items():
    #     print(key)
    #     print(value)
    # print(temp)

#write_con(url)

#coding:utf-8
import pandas as pd


#print(df)

date_list=[20200110,20200111,20200112,20200113,20200114,20200115,20200116,20200117,20200118,20200119,20200120,20200121,20200122,20200123,20200124,20200125,20200126,20200127,20200128,20200129,20200130
]
#df[1][1]=5

dd_url='http://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id={id}&type=move_out&startDate=20200101&endDate=20200130'
#单独的url

def return_list(code):
    t_url=dd_url.format(id=code)
    print(t_url)
    data=write_con(t_url)
    print(data)
    result=[]
    for t in date_list:
        result.append(data[str(t)])
    return result
def main_func():
    filename = 'result.csv'
    df_obj = pd.read_csv(r'E:\Githubresponsity\毕业论文\获取流量\输出去重带纠偏经纬度.csv', engine='python', sep=',',
                         encoding="utf_8_sig")

    area = df_obj['area'].values
    code = df_obj['code'].values

    data = {
        'area': area,
        'code': code
    }
    df = pd.DataFrame(data, index=None)

    df['20200110'] = None
    df['20200111'] = None
    df['20200112'] = None
    df['20200113'] = None
    df['20200114'] = None
    df['20200115'] = None
    df['20200116'] = None
    df['20200117'] = None
    df['20200118'] = None
    df['20200119'] = None
    df['20200120'] = None
    df['20200121'] = None
    df['20200120'] = None
    df['20200121'] = None
    df['20200122'] = None
    df['20200123'] = None
    df['20200124'] = None
    df['20200125'] = None
    df['20200126'] = None
    df['20200127'] = None
    df['20200128'] = None
    df['20200129'] = None
    df['20200130'] = None

    for i in range(len(area)):
        try:
            t_url=url.format(id=code[i])
            #print(t_url)
            t_data=write_con(t_url)
            #print(t_data)
            for j in date_list:
                df.at[i,j]=t_data[j]
            time.sleep(0.1)
        except:
            print('error')
            print(area[i])
    df.to_csv(filename, index=None, encoding="utf_8_sig")

print(return_list(430100))
