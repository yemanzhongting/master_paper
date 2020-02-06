# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/1/31 17:05'
import re
from 坐标纠偏 import bd09togcj02,gcj02towgs84
city_name= ['武汉市','嘉峪关市', '金昌市', '白银市', '兰州市', '酒泉市', '大兴安岭地区', '黑河市', '伊春市', '齐齐哈尔市', '佳木斯市', '鹤岗市', '绥化市', '双鸭山市', '鸡西市',
        '七台河市', '哈尔滨市', '牡丹江市', '大庆市', '白城市', '松原市', '长春市', '延边朝鲜族自治州', '吉林市', '四平市', '白山市', '沈阳市', '阜新市', '铁岭市',
        '呼伦贝尔市', '兴安盟', '锡林郭勒盟', '通辽市', '海西蒙古族藏族自治州', '西宁市', '海北藏族自治州', '海南藏族自治州', '海东地区', '黄南藏族自治州', '玉树藏族自治州',
        '果洛藏族自治州', '甘孜藏族自治州', '德阳市', '成都市', '雅安市', '眉山市', '自贡市', '乐山市', '凉山彝族自治州', '攀枝花市', '和田地区', '喀什地区',
        '克孜勒苏柯尔克孜自治州', '阿克苏地区', '巴音郭楞蒙古自治州', '博尔塔拉蒙古自治州', '吐鲁番地区', '伊犁哈萨克自治州', '哈密地区', '乌鲁木齐市', '昌吉回族自治州', '塔城地区',
        '克拉玛依市', '阿勒泰地区', '山南地区', '林芝地区', '昌都地区', '拉萨市', '那曲地区', '日喀则地区', '阿里地区', '昆明市', '楚雄彝族自治州', '玉溪市', '红河哈尼族彝族自治州',
        '普洱市', '西双版纳傣族自治州', '临沧市', '大理白族自治州', '保山市', '怒江傈僳族自治州', '丽江市', '迪庆藏族自治州', '德宏傣族景颇族自治州', '张掖市', '武威市', '东莞市',
        '东沙群岛', '三亚市', '鄂州市', '乌海市', '莱芜市', '海口市', '蚌埠市', '合肥市', '阜阳市', '芜湖市', '安庆市', '北京市', '重庆市', '南平市', '泉州市', '庆阳市',
        '定西市', '韶关市', '佛山市', '茂名市', '珠海市', '梅州市', '桂林市', '河池市', '崇左市', '钦州市', '贵阳市', '六盘水市', '秦皇岛市', '沧州市', '石家庄市',
        '邯郸市', '新乡市', '洛阳市', '商丘市', '许昌市', '襄阳市', '荆州市', '长沙市', '衡阳市', '镇江市', '南通市', '淮安市', '南昌市', '新余市', '通化市', '锦州市',
        '大连市', '乌兰察布市', '巴彦淖尔市', '渭南市', '宝鸡市', '枣庄市', '日照市', '东营市', '威海市', '太原市', '文山壮族苗族自治州', '温州市', '杭州市', '宁波市',
        '中卫市', '临夏回族自治州', '辽源市', '抚顺市', '阿坝藏族羌族自治州', '宜宾市', '中山市', '亳州市', '滁州市', '宣城市', '廊坊市', '宁德市', '龙岩市', '厦门市',
        '莆田市', '天水市', '清远市', '湛江市', '阳江市', '河源市', '潮州市', '来宾市', '百色市', '防城港市', '铜仁地区', '毕节地区', '承德市', '衡水市', '濮阳市',
        '开封市', '焦作市', '三门峡市', '平顶山市', '信阳市', '鹤壁市', '十堰市', '荆门市',  '常德市', '岳阳市', '娄底市', '株洲市', '盐城市', '苏州市',
        '景德镇市', '抚州市', '本溪市', '盘锦市', '包头市', '阿拉善盟', '榆林市', '铜川市', '西安市', '临沂市', '滨州市', '青岛市', '朔州市', '晋中市', '巴中市',
        '绵阳市', '广安市', '资阳市', '衢州市', '台州市', '舟山市', '固原市', '甘南藏族自治州', '内江市', '曲靖市', '淮南市', '巢湖市', '黄山市', '淮北市', '三明市',
        '漳州市', '陇南市', '广州市', '云浮市', '揭阳市', '贺州市', '南宁市', '遵义市', '安顺市', '张家口市', '唐山市', '邢台市', '安阳市', '郑州市', '驻马店市',
        '宜昌市', '黄冈市', '益阳市', '邵阳市', '湘西土家族苗族自治州', '郴州市', '泰州市', '宿迁市', '宜春市', '鹰潭市', '朝阳市', '营口市', '丹东市', '鄂尔多斯市',
        '延安市', '商洛市', '济宁市', '潍坊市', '济南市', '上海市', '晋城市', '南充市', '丽水市', '绍兴市', '湖州市', '北海市', '赤峰市', '六安市', '池州市', '福州市',
        '惠州市', '江门市', '汕头市', '梧州市', '柳州市', '黔南布依族苗族自治州', '保定市', '周口市', '南阳市', '孝感市', '黄石市', '张家界市', '湘潭市', '永州市', '南京市',
        '徐州市', '无锡市', '吉安市', '葫芦岛市', '鞍山市', '呼和浩特市', '吴忠市', '咸阳市', '安康市', '泰安市', '烟台市', '吕梁市', '运城市', '广元市', '遂宁市',
        '泸州市', '天津市', '金华市', '嘉兴市', '石嘴山市', '昭通市', '铜陵市', '肇庆市', '汕尾市', '深圳市', '贵港市', '黔东南苗族侗族自治州', '黔西南布依族苗族自治州',
        '漯河市', '扬州市', '连云港市', '常州市', '九江市', '萍乡市', '辽阳市', '汉中市', '菏泽市', '淄博市', '大同市', '长治市', '阳泉市', '马鞍山市', '平凉市',
        '银川市', '玉林市', '咸宁市', '怀化市', '上饶市', '赣州市', '聊城市', '忻州市', '临汾市', '达州市', '宿州市', '随州市', '德州市', '恩施土家族苗族自治州', '阿拉尔市',
        '石河子市', '五家渠市', '图木舒克市', '定安县', '儋州市', '万宁市', '保亭黎族苗族自治县', '西沙群岛', '济源市', '潜江市', '中沙群岛', '南沙群岛', '屯昌县',
        '昌江黎族自治县', '陵水黎族自治县', '五指山市', '仙桃市', '琼中黎族苗族自治县', '乐东黎族自治县', '临高县', '琼海市', '白沙黎族自治县', '东方市', '天门市', '神农架林区',
        '澄迈县', '文昌市', '澳门特别行政区', '香港特别行政区', '桃园市', '台北市', '南投县', '嘉义市', '彰化县', '新竹县', '澎湖县', '台东县', '宜兰县', '新北市', '基隆市',
        '屏东县', '嘉义县', '云林县', '花莲县', '台南市', '台中市', '新竹市', '高雄市', '苗栗县']

class step1():
    def step1(self):
        with open('地区.txt','r',encoding='utf-8') as f:
            texts=f.readlines()

        with open('输出.txt','w+',encoding='utf-8') as w:
            # texts=f.readlines()
            for i in texts:
                for j in city_name:
                    if j[:-1] in i:
                        number=re.findall(r"\d+\.?\d*", i)[0]
                        w.write(j)
                        w.write(',')
                        w.write(number)
                        w.write('\n')

        with open('输出.txt','r',encoding='utf-8') as r:
            tmp=r.readlines()

        result=list(set(tmp))

        with open('输出去重.txt','w+',encoding='utf-8') as r:
            for i in result:
                r.write(i)
                #r.write('\n')

#################此部分负责输出
import json,time
import pandas as pd
from urllib.request import urlopen, quote
class step2():
    def getlnglat(address):
        #http://api.map.baidu.com/geocoder/v2/?address=北京市海淀区上地十街10号&output=json&ak=您的ak&callback=showLocation //GET请求
        url = 'http://api.map.baidu.com/geocoder/v2/'
        output = 'json'
        ak = '8399wyuCP00HcW0c7rHfjMpCIT6dA4mC' # 浏览器端密钥
        address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
        uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak
        print(uri)
        req = urlopen(uri)
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
            lat.append(round(t_geocode[1],8))#lat
            lng.append((round(t_geocode[0],9)))#lng

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


if __name__ == '__main__':
    s=step2()
    #s.