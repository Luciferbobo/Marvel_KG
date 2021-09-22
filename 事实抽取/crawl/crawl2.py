# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

import requests
import bs4
import json

url = 'https://graphics.straitstimes.com/STI/STIMEDIA/Interactives/2018/04/marvel-cinematic-universe-whos-who-interactive/data/marvel-data.json'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
response = requests.get(url=url, headers=headers)
result = json.loads(response.text)

num = 0
names = []
item = {0: 'friend', 1: 'enemy', 2: 'creation', 3: 'family', 4: 'work', 5: 'love'}

for i in result['relationship']:
    subject = result['relationship'][i]['id']
    object = result['relationship'][i]['target_id']

    if subject not in names:
        names.append(subject)
    if object not in names:
        names.append(object)

    relation = int(result['relationship'][i]['relationship'])
    with open('./relation_message.csv', 'a+') as f:
        f.write(subject + ',' + object + ',' + item[relation] + '\n')

for j in names:
    num += 1
    with open('./names_message.csv', 'a+') as f:
        f.write(j + ',' + str(num) + '\n')

for k in result['characters']:
    id = result['characters'][k]['id']
    name = result['characters'][k]['name']
    status = result['characters'][k]['status']
    species = result['characters'][k]['species']
    with open('./message.csv', 'a+') as f:
        f.write(id + ',' + name + ',' + status + ',' + species + '\n')



for n in result['alter_ego']:
    id = result['alter_ego'][n]['origin_id']
    name = result['alter_ego'][n]['name']
    str = ''
    movie = result['alter_ego'][n]['movie_involved']
    for i in movie.keys():
        if(movie[i]):
            str=str+i+'/'
    with open('./movie.csv','a+') as f:
        f.write(id+ ','+ name+ ','+str +'\n')