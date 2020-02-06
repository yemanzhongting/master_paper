__author__ = 'zy'
__time__ = '2020/2/1 13:05'
import pandas as pd
city_name = ['武汉', '仙桃','天门','神农架','潜江','黄石', '十堰', '宜昌', '襄阳', '鄂州', '荆门', '孝感', '荆州', '黄冈', '咸宁', '随州', '恩施']

df=pd.read_csv('out.txt',engine='python', sep=',',
                         encoding="utf_8_sig",header=None)

df.columns=['from','to','province','percent']

from_city=[]
to_city=[]
value=[]

for index, row in df.iterrows():
    for i in city_name:
        if i in row['from']:
            for j in city_name:
                if j in row['to']:
                    tmp=row.values.tolist()
                    from_city.append(tmp[0])
                    to_city.append(tmp[1])
                    value.append(tmp[3])

data = {'from':from_city,'to':to_city,'percent':value}
df_data = pd.DataFrame(data, index=None)

df_data['number']=None
df_data['absvalue']=None
df_data['lat']=None
df_data['lng']=None
df_data['source']=None
df_data['target']=None


#df.at[i,j]=t_data[j]
df_value=pd.read_csv('hubei.csv',engine='python', sep=',',
                         encoding="utf_8_sig")

print(list(set(df_data['from'].values.tolist())))

city_name=['咸宁市', '随州市', '仙桃市', '黄石市', '神农架林区', '荆门市', '潜江市', '孝感市', '鄂州市', '荆州市', '恩施土家族苗族自治州', '十堰市', '黄冈市', '襄阳市', '天门市', '武汉市', '宜昌市']


city_latlng=[[29.841199638680287,114.32200002765934],[31.69030058523121,113.38299957624614]
             ,[30.327808562443895,113.4430708646698],[30.19939960293492,115.03900003418904]
             ,[31.74460031047552,110.67599978780419],[31.03539989309376,112.20000022843752]
             ,[30.40220042749318,112.89899997927145],[30.92480004292067,113.91599992196133]
             ,[30.390900497976883,114.89499986501862],[30.335000380826443,112.23899990797712]
             ,[30.272200939196907,109.4879997112762],[32.62920058688821,110.79800000487187]
             ,[30.45339975507176,114.87200001362683],[32.00900052477173,112.12199980021491],
             [30.663299439124792,113.1660004274518],[30.592799572064738,114.30500043085405],[30.691700466222986,111.28599985191957]]




date='20200120'#area,code,20200101,

for index, row in df_value.iterrows():#绝对值
    for index2, row2 in df_data.iterrows():#相对 值神农架林区
        # print(row['area'])
        # print(row2['from'])
        # print('##')
        if row['area']==row2['from']:
            for key in city_name:
                if row['area']==key:
                    t_index=city_name.index(key)
                    df_data.at[index2, 'lat']=city_latlng[t_index][0]
                    df_data.at[index2, 'lng'] = city_latlng[t_index][1]

            print('一致')
            print(row[date])
            df_data.at[index2, 'number'] =row[date]
            df_data.at[index2, 'absvalue'] = row[date]*row2['percent']/100

print(df_data)

for index, row in df_data.iterrows():  # 相对 值神农架林区
    for i in city_name:
        i_index=city_name.index(i)
        if row['from'] == i:
            df_data.at[index, 'source']=i_index
        if row['to'] == i:
            df_data.at[index, 'target']=i_index

df_data.to_csv('out0120.csv', index=None, encoding="utf_8_sig")




