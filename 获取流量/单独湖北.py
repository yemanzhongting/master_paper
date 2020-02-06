# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/1/31 21:48'
import time

__author__ = 'zy'
__time__ = '2020/1/31 20:23'
import requests,re,json
url='http://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id={id}&type=move_in&startDate=20200101&endDate=20200130'
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

date_list=[20200101,20200102,20200103,20200104,20200105,20200106,20200107,20200108,20200109,20200110,20200111,20200112,20200113,20200114,20200115,20200116,20200117,20200118,20200119,20200120,20200121,20200122,20200123,20200124,20200125,20200126,20200127,20200128,20200129,20200130
]
import pandas as pd
def main_func():
    city_name = ['武汉', '仙桃','天门','神农架','潜江','黄石', '十堰', '宜昌', '襄阳', '鄂州', '荆门', '孝感', '荆州', '黄冈', '咸宁', '随州', '恩施']

    filename = 'hubei_in.csv'
    df_obj = pd.read_csv(r'E:\Githubresponsity\毕业论文\获取流量\输出去重带纠偏经纬度.csv', engine='python', sep=',',
                         encoding="utf_8_sig")

    area = df_obj['area'].values
    code = df_obj['code'].values

    hb_area=[]
    hb_code=[]
    for i in range(len(area)):
        for j in city_name:
            if j in area[i]:
                hb_area.append(area[i])
                hb_code.append(code[i])
    data = {
        'area': hb_area,
        'code': hb_code
    }

    df = pd.DataFrame(data, index=None)

    df['20200101'] = None
    df['20200102'] = None
    df['20200103'] = None
    df['20200104'] = None
    df['20200105'] = None
    df['20200106'] = None
    df['20200107'] = None
    df['20200108'] = None
    df['20200109'] = None
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

    print(data)
    print('###')
    print(df)
    for i in range(len(hb_area)):
        try:
            t_url=url.format(id=hb_code[i])
            #print(t_url)
            t_data=write_con(t_url)
            #print(t_data)
            for j in date_list:
                j=str(j)
                try:
                    df.at[i,j]=t_data[j]
                except:
                    df.at[i, j]=None
            time.sleep(0.1)
        except:
            print('error')
            print(area[i])
    print(df)
    df.to_csv(filename, index=None, encoding="utf_8_sig")

if __name__ == '__main__':
    main_func()

