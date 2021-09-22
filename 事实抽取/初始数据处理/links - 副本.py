import pandas as pd
import collections
import json
import random

id_data=pd.read_excel('message_small.xlsx',header=None)
#id_data=pd.read_csv('message.csv',header=None)
id_data = collections.OrderedDict(zip(id_data.iloc[:,0],id_data.iloc[:,2]))
id_data=dict(id_data)

relation=pd.read_csv('relation_message.csv',header=None)
relation=relation.replace(['friend', 'family', 'work', 'enemy', 'love'], 
                          ['朋友', '家人', '共事', '敌人', '爱人'])
relation_pro=pd.DataFrame(columns=(0,1,2))
for i in range(len(relation)):
    if (relation.iloc[i][0] in list(id_data.keys())) and (relation.iloc[i][1] in list(id_data.keys())):
        relation_pro=relation_pro.append([{0:relation.iloc[i][0],1:relation.iloc[i][1],2:relation.iloc[i][2]}])
for i in range(len(relation_pro)):
    relation_pro.iloc[i][0]=id_data[relation_pro.iloc[i][0]]
    relation_pro.iloc[i][1]=id_data[relation_pro.iloc[i][1]]

num = dict(zip(list(id_data.values()),[i for i in range(1,len(id_data.values())+1)]))

with open('relation.json',encoding='utf-8') as f:
    ori = json.load(f)

#name
p1=[]
for i in range(len(num)):
    p1.append({'name':list(num.keys())[i],'category':random.randint(0,5)})
    
#relation
p2=[]
for i in range(len(relation_pro)):
    p2.append({'source': num[relation_pro.iloc[i][0]], 'target': num[relation_pro.iloc[i][1]], 'value': relation_pro.iloc[i][2]})
    print(relation_pro.iloc[i][0],relation_pro.iloc[i][1],relation_pro.iloc[i][2])
result={'data':p1,'links':p2}
b = json.dumps(result,ensure_ascii=False)
f2 = open('data.json', 'w',encoding='utf-8')
f2.write(b)
f2.close()
