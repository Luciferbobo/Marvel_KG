# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:30:53 2021

@author: 17112
"""

list01 = []
for i in open('relation.txt',encoding='utf8'):
    if i in list01:
        continue
    list01.append(i)
    j=i.split(',')
    temp=j[0]
    j[0] = j[1]
    j[1]=temp
    list01.append(','.join(j))
with open('test01.txt', 'w',encoding='utf8') as handle:
    handle.writelines(list01)
