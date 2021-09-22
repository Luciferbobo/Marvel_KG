import json as json
baidujson=[]
f= open('data.json',encoding='utf8')
baidujson = json.load(f)
#print(baidujson)

wikiheros=['美国队长','绿巨人','雷神','黑寡妇','战争机器','鹰眼','尼克弗瑞','猎鹰','幻视','绯红女巫','快银','奥创','特工希尔','特工卡特','海姆达尔','小辣椒','霍华德·史塔克','玛丽亚·斯塔克','埃德温·贾维斯','奥丁','希芙','特查拉','灭霸','星爵','卡魔拉','毁灭者德拉克斯','火箭浣熊','格鲁特','勇度','星云','罗南','黄蜂女','伊戈','银影侠','格鲁特','蚁人','初代蚁人','黄蜂侠','奇异博士','莫度男爵','古一','彼得·帕克','梅·帕克','闪电·汤普森','乌木喉','黑矮星']

wikijson=[]
f2= open('wiki.json',encoding='utf8')
wikijson = json.load(f2)

for i in wikiheros:
    print(wikijson[i])
    print(baidujson[i])
