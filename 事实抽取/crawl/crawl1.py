import json
import requests
 
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
 
url = 'https://graphics.straitstimes.com/STI/STIMEDIA/Interactives/2018/04/marvel-cinematic-universe-whos-who-interactive/data/marvel-data.json'
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
    with open('relation_message.csv', 'a+') as f:
        f.write(subject + ',' + object + ',' + item[relation] + '\n')
 
for j in names:
    num += 1
    with open('names_message.csv', 'a+') as f:
        f.write(j + ',' + str(num) + '\n')
 
for k in result['characters']:
    id = result['characters'][k]['id']
    name = result['characters'][k]['name']
    status = result['characters'][k]['status']
    species = result['characters'][k]['species']
    with open('message.csv', 'a+') as f:
        f.write(id + ',' + name + ',' + status + ',' + species + '\n')
