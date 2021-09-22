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
import re

def get_url(name_list):
	url_list = []
	for i in range(len(name_list)):
		url = 'https://baike.baidu.com/item/' + str(name_list[i]) + '?force=1'
		url = quote(url, safe=string.printable)

		req = request.Request(url, headers=headers)
		response = request.urlopen(req, timeout=20)
		html = response.read().decode('utf-8')
		soup = BeautifulSoup(html, 'html.parser', )
		find = soup.find_all(class_="list-dot list-dot-paddingleft")
		# print(res_key[0])
		# key = [ik.get_text().strip().replace("\n", "、") for ik in res_key]
		# print(key)
		if len(find) == 0 or len(find) == 1:
			url_list.append([''.join(name_list[i]),url])
		else:
			# print(find)
			if len(find) != 0:
				for x in find:
					str1 = str(x)
					if ('漫威漫画旗下' in str1 or '美国漫威漫画下' in str1):
						index1 = re.search('href=', str1).span()[1]
						index2 = re.search('target', str1).span()[0]
						url_save = 'https://baike.baidu.com' + str1[index1 + 1:index2 - 2]
						url_list.append([''.join(name_list[i]),url_save])
	test = pd.DataFrame(data=url_list)
	test.to_csv('testcsv.csv', encoding='utf-8')







if __name__ == "__main__":
	headers = {}
	headers[
		"User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
	data = pd.read_excel('url.xlsx', header=None,engine='openpyxl')
	# data_url = data.values[:, 3]
	data_name = data.values[:, 2]
	name_list = data_name.tolist()
	# url_list = data_url.tolist()

	get_url(name_list)
