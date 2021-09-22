import requests
from lxml import etree
import numpy as np
import random 
import re
import json
import pandas as pd
import matplotlib.pyplot as plt
from urllib import request

data=pd.read_excel('url.xlsx',header=None)
name=data.values[:5,2]
data=data.values[:5,3]
url_list=data.tolist()


UA_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36']



head = random.choice(UA_list)
header = {'User-Agent':head}
old_url = [] #已经爬取过的

with open('./dirty_data.json', 'w',encoding='utf-8') as json_file:
    pass#清空文件

for i_d in range(len(url_list)):
    url = url_list[i_d]
    if url in old_url:
        continue
    response = requests.get(url=url,headers = header)
    pagetext = response.text
    tree = etree.HTML(pagetext)
    basicinfo_tmp = tree.xpath('//dt[@class="basicInfo-item name"]/text()')
    basicinfo = []
    for i in basicinfo_tmp:
        line = i.strip()  
        p2 = re.compile('[^\u4e00-\u9fa5]') 
        zh = "".join(p2.split(line)).strip()
        basicinfo.append(zh)

    basicinfovalue = tree.xpath('//dd[@class="basicInfo-item value"]//text()')

    experience = ''
    for tmp in tree.xpath('//div[@class="para"]//text()'):
        experience +=tmp
    pic = tree.xpath('//div[@class="summary-pic"]//img/@src')
    #print(pic)
    #pic='http://bkimg.cdn.bcebos.com/pic/962bd40735fae6cd7b898baabaf8182442a7d833a1ef?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg'
    #img = request.urlopen(pic,headers=header)
    pic=pic.encode('utf8')
    plt.show(img)
    img_name=name[i_d]
    with open('./image/'+img_name+'.jpg','wb') as f:
        f.write(img)
    power = tree.xpath('//div/table[@log-set-param="table_view"]//text()')
    tmp_dict = {
        'id':i_d+1,
        'basicinfo': basicinfo,
        'basicinfovalue': basicinfovalue,
        #'experience':experience,
        'power':power
    }
    json_str = json.dumps(tmp_dict,ensure_ascii=False)
    #print(json_str)
    print(i_d+1)

    with open('./dirty_data.json', 'a',encoding='utf-8') as json_file:
         json_file.write(json_str)
         json_file.write('\n')
    
    old_url.append(url)




