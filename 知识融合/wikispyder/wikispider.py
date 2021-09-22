#!/usr/bin/env python
# coding:utf8

from urllib import request
from urllib.parse import quote
import  string
import time
import json
from bs4 import BeautifulSoup
import codecs
from get_character_array import get_character
import os
import pandas as pd
headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
def listToJson(lst):
    import json
    import numpy as np
    keys = [str(x) for x in np.arange(len(lst))]
    list_json = dict(zip(keys, lst))
    str_json = json.dumps(list_json, indent=2, ensure_ascii=False)  # json转为string
    return str_json


if __name__ == "__main__":
	df = pd.read_csv("mavelurl.csv",index_col=False)
	urls = df.iloc[:, 3:4].values.tolist()
	name = df.iloc[:, 2:3].values.tolist()
	#print(name,urls)
	#print(name,urls)
	no_url=[]
	fail_name = []
	fail_url=[]
	svfile = {}
	f = codecs.open('wikidata.json', 'w', 'utf-8')
	f.truncate()

	un_name=[]
	for i in range(len(urls)):
		if (''.join(name[i]) not in un_name):
			#print(name[i])
		
			#print(name[i],str(urls[i][0]))
			if urls[i][0] == '0':
				no_url.append(name[i])
				#print("info not found")
				continue
			print(''.join(name[i]))
			req = request.Request(str(urls[i][0]), headers=headers)
			response = request.urlopen(req, timeout=20)
			
			html = response.read().decode('utf-8')
			soup = BeautifulSoup(html, 'html.parser')
			infobox = soup.find_all(True, {"class": ["infobox"]})
			if len(infobox) == 0:
				fail_name = []
				fail_url=[]
				#print('failed to find infobox')

				#svfile[''.join(name[i])]=""
			else:
				key=name[i]
				value = [iv.get_text().strip().replace("\n", "、") for iv in infobox]
				svfile[''.join(name[i])]=str(value[0])
	#f.write(json.dumps(svfile,  ensure_ascii=False))
