# -*- coding:utf-8 -*-
import requests
import pandas as pd

'''
def translate(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'false'}
    # 将需要post的内容，以字典的形式记录在data内。
    r = requests.post(url, data=data)
    # post需要输入两个参数，一个url，一个是data，返回的是一个Response对象
    answer = r.json()
    result = answer['translateResult'][0][0]['tgt']
    #print('"'+ word + '"的翻译结果：' + result + '\n')
    return result

if __name__=="__main__":
    data=pd.read_csv('relation_message.csv',header=None)
    data=data.values[0:10]
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j]=translate(data[i][j])
'''


url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
r=requests.get(url)