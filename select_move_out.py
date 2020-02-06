# -*- coding: UTF-8 -*-
import re

__author__ = 'zy'
__time__ = '2020/1/31 12:50'
import os

def file_name(file_dir):

    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件

    print('---------')
    print(files)
    return files

def deal_with_download_file(root_source):

    file_list = file_name(root_source)

    os.chdir(root_source)
    # 查看修改后的工作目录
    retval = os.getcwd()
    print(retval)

    cmds = []

# list1 = ["这", "是", "一个", "测试"]
# for index, item in enumerate(list1):
#     print index, item

city_list=[]
with open('20200124.txt','r',encoding='utf-8') as f:
    texts=f.readlines()

#print(texts)
with open('out24.txt','w+',encoding='utf-8') as wr:
    for index,item in enumerate(texts):
        if 'move_out' in item:
            for j in texts[index+1:index+51]:
                if (re.findall(r"\d+\.?\d*", j))!=[]:
                    wr.write(j)
                    print(j)
        #wr.write('\n')

city_name = ['武汉', '黄石', '十堰', '宜昌', '襄阳', '鄂州', '荆门', '孝感', '荆州', '黄冈', '咸宁', '随州', '恩施']

    # f.close()
    # tmp=f.readline()
    # print(tmp)
    # if 'move_out' in tmp:
    #     print(tmp[line+1:line+51])

#print(tmp)

line=0
# for i in tmp:
#     #tmp[line]=tmp[line][:-2]
#     line=line+1

#print(tmp)

# with open('1.txt','w+') as q:
#     for j in tmp:
#         q.write(j)


out_list=['苗栗县','高雄市','新竹市','台中市','台南市','花莲县','云林县','嘉义县','屏东县','基隆市','新北市',
          '宜兰县','台东县','澎湖县','新竹县','彰化县','嘉义市','南投县','台北市','桃园市']
# for i in tmp:
#     #tmp[line].replace('\n', '')
#     if 'move_out' in i:
#         print(tmp[line+1:line+51])