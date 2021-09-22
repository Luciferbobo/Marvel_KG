#!/usr/bin/env python


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
if not os.path.exists("./spider/test"):
		os.mkdir("./spider/test")



def get_json(name_list,url_list):
	data={}
	for i in range(len(name_list)):
		url = url_list[i]
		url = quote(url, safe=string.printable)
		req = request.Request(url, headers=headers)
		response = request.urlopen(req, timeout=20)
		try:
			html = response.read().decode('utf-8')
			soup = BeautifulSoup(html, 'html.parser', )
			res = soup.find(class_="summary-pic")
			pic_name = name_list[i] + '.jpg'
			img_src = res.find('img').get('src')
			request.urlretrieve(img_src, pic_name)
		except:
			print("找不到图片")
		res_key = soup.find_all(class_="basicInfo-item name")
		res_val = soup.find_all(class_="basicInfo-item value")

		res_val2 = soup.find_all(attrs={'log-set-param':"table_view",'data-sort':"sortDisabled"})
		value2 = [iv.get_text().strip().replace("\n", "、") for iv in res_val2]


		key = [ik.get_text().strip().replace("\n", "、") for ik in res_key]
		key.append('经历')
		key.append('能力')
		value = [iv.get_text().strip().replace("\n", "、") for iv in res_val]

		# 经历
		res_val1 = soup.find_all(class_="para")
		value3 =[iv.get_text().strip().replace("\n", "、") for iv in res_val1]
		str_re = ''
		for j in range(len(value3)):
			str_re += value3[j]
		value.append(str_re)
		for x in value2:
			if '智力' in x and '属性备注' not in x and '战斗技能' in x:
				value.append(x)
		item = dict(zip(key, value))
		data[name_list[i]] = item
		print(name_list[i])
	if not os.path.exists("../json"):
		os.mkdir("../json")
	f = codecs.open('../json/data.json', 'w', 'utf-8')
	f.write(json.dumps(data, ensure_ascii=False))


	# for i in set(character_arr):
	# 	print(i)
	# 	#url= r'https://baike.baidu.com/item/'+i
	# 	url=r'https://baike.baidu.com/item/%E6%96%AF%E7%A7%91%E5%B0%94%E5%A5%87?fromtitle=Skurge&fromid=22617538'
	# 	url = quote(url, safe = string.printable)
	# 	req = request.Request(url, headers=headers)
	# 	response = request.urlopen(req, timeout=20)
	#
	# 	try:
	# 		html = response.read().decode('utf-8')
	# 		soup = BeautifulSoup(html, 'html.parser', )
	# 		res = soup.find(class_="summary-pic")
	# 		pic_name = str(i) + '.jpg'
	# 		img_src = res.find('img').get('src')
	# 		request.urlretrieve(img_src,pic_name)
	# 	except :
	# 		print("找不到图片")
	# 	res_key=soup.find_all(class_ ="basicInfo-item name")
	# 	res_val=soup.find_all(class_ ="basicInfo-item value")
	# 	key=[ik.get_text().strip().replace("\n","、") for ik in res_key]
	# 	value = [iv.get_text().strip().replace("\n", "、") for iv in res_val]
	# 	item=dict(zip(key,value))
	# 	print(key)
	# 	data[str(i)]=item
	# if not os.path.exists("../json"):
	# 	os.mkdir("../json")
	# f = codecs.open('../json/data.json','w','utf-8')
	# f.write(json.dumps(data,  ensure_ascii=False))
if __name__ == "__main__":
	#character_arr=get_character()
	#character_arr = ['钢铁侠','蜘蛛侠','冬兵','黑寡妇','彼得帕克']
	# character_arr = ['彼得帕克']
	headers = {}
	headers[
		"User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
	data = pd.read_excel('url.xlsx', header=None)
	data_url = data.values[:, 3]
	data_name = data.values[:, 2]
	name_list = data_name.tolist()
	url_list = data_url.tolist()
	os.chdir(os.path.join(os.getcwd(), './spider/test'))
	get_json(name_list,url_list)
