import jieba
import tqdm
f = open("./wiki_zh_10_sim.txt","r",encoding='UTF-8')
lines = f.readlines()
result = open('results.txt', 'w', encoding='UTF-8')
jieba.load_userdict('./test.txt')
#读取全部内容 ，并以列表方式返回
for line in lines:
    words = jieba.lcut(line)
    result.write('  '.join(words))
result.close()


