#!/usr/bin/env python
# coding: utf-8
import requests
from lxml import etree
import numpy as np
import random 
import re
import json

#基于角色经历-正则进行类别推断
#1：复仇者联盟 2:神盾局特工 3:银河护卫队
def textmatch_2(string):
    pattern_1 = re.compile('(.*)[\u52a0][\u5165](.*)[\u590d][\u4ec7][\u8005](.*)$')
    pattern_2 = re.compile('(.*)[\u52a0][\u5165](.*)[\u795e][\u76fe][\u5c40](.*)$')
    pattern_3 = re.compile('(.*)[\u52a0][\u5165](.*)[\u94f6][\u6cb3][\u62a4][\u536b][\u961f](.*)$')
    if(pattern_1.search(string)):
        return '1'
    if(pattern_2.search(string)):
        return '2'
    if(pattern_3.search(string)):
        return '3'
    return '5'
    
def textmatch_1(basicinfo,basicinfo_value):
    pattern_4 = re.compile('(.*)[\u8d85][\u7ea7][\u53cd][\u6d3e][\u000d][\u000a](.*)$')
    idx = 0
    for i in range(len(basicinfo)):
        if basicinfo[i] =='所属团队':
           idx = i
        break
    if(pattern_4.search(basicinfo_value[i])):
        return '4'
    else:
        return '0'
        
#基于infobox进行类别推断 4：超级反派
url_list = ['https://baike.baidu.com/item/%E7%BB%AF%E7%BA%A2%E5%A5%B3%E5%B7%AB/10120741','https://baike.baidu.com/item/%E5%B9%BB%E8%A7%86/15388599']

UA_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36']
head = random.choice(UA_list)
header = {'User-Agent':head}
old_url = [] #已经爬取过的
for i_d in range(len(url_list)):
    url = url_list[i_d]
    if url in old_url:
        continue
    response = requests.get(url=url,headers = header)
    pagetext = response.text
    tree = etree.HTML(pagetext)
    #基本信息 ['中文名','外文名','别名','国籍','出生地', '身高','体重', '职业','代表作品','主要成就','所属团队','主要能力', '配偶','身份']
    basicinfo_tmp = tree.xpath('//dt[@class="basicInfo-item name"]/text()')
    basicinfo = []
    for i in basicinfo_tmp:
        line = i.strip()  
        p2 = re.compile('[^\u4e00-\u9fa5]') 
        zh = "".join(p2.split(line)).strip()
        basicinfo.append(zh)

    basicinfovalue = tree.xpath('//dd[@class="basicInfo-item value"]//text()')
    #角色经历
    experience = ''
    for tmp in tree.xpath('//div[@class="para"]//text()'):
        experience +=tmp
    #人物图片url
    pic = tree.xpath('//div[@class="summary-pic"]//img/@src')
    #能力值
    power = tree.xpath('//div/table[@log-set-param="table_view"]//text()')
    tmp_dict = {
        'id':i_d,
        'basicinfo': basicinfo,
        'basicinfovalue': basicinfovalue,
        'experience':experience,
        'power':power
    }
    json_str = json.dumps(tmp_dict,ensure_ascii=False)
    #print(json_str)
    print(i_d)
    with open('./dirty_data.json', 'a',encoding='utf-8') as json_file:
         json_file.write(json_str)
    old_url.append(url)
    



