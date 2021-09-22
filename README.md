# 漫威知识图谱 Marvel knowledge graph

## 一.配置环境

1. 配置环境以及安装neo4j，python版本需为3.6
2. 控制台输入 "neo4j console" 启动neo4j
3. 修改“KG_Marvel\neo_db\config.py”中的用户名密码
4. 解压“KG_Marvel\KGQA\ltp_data_v3.4.0.zip”
5. 修改“KG_Marvel\KGQA\ltp.py”中的模型路径（需用绝对路径）
6. 运行“KG_Marvel\neo_db\creat_graph.py”，将关系传入数据库
7. 运行  "KG_Marvel\app.py"
8. 浏览器输入“http://localhost:5000/”，进入知识图谱。

## 二.文件描述

- KGQA: 储存了基于ltp模型的分词函数
- neo_db: 建立neo4j数据库
- spyder：储存超级英雄个人信息和图片以及关系
- static: 网页中用到的图片字体等
- templates: 网页脚本
- app.py: 启动知识图谱

## 三.算法说明

### 1.事实抽取

- crawl存放爬虫文件，get_hlm_character.py、spider_url.py等进行信息抽取，外网数据.py为后期信息补充
- 初始数据处理文件夹记录了数据清洗过程

### 2.知识融合

- wikispyder找到维基百科中漫威领域对应数据
- fusion进行知识融合

### 3.类别推断

- Type_Inference.py进行基于规则的类别推断

### 4.知识问答

- FLAT模型包含FLAT命名实体识别模型
- ltp.py为LTP中文分词库的调用实现

### 5.推荐系统

- WMSeg-sota分词包含WMSeg分词算法的实现
- word2vec.ipynb计算词向量，找到最合适的推荐实体



