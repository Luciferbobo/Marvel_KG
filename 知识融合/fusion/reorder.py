# coding=utf-8
import json as json
import codecs



wikijson=[]
f2= open('fusion.json',encoding='utf8')
wikijson = json.load(f2)
heros=[]
for i in wikijson:
     heros.append(i)
for i in heros:
    del wikijson[i]['经历']
    
w = codecs.open('reorder.json', 'w', 'utf-8')
w.write(json.dumps(wikijson,  ensure_ascii=False))