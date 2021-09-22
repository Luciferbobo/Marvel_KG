# Marvel_KG
漫威知识图谱 Marvel Knowledge Graph
## 1.文件树:<br>
1)  app.py 知识图谱主入口<br>
2)  templates文件夹是HTML页面<br>
     |-index.html 初始菜单<br> 
     |-search.html 搜索人物关系页面<br>
     |-all_relation.html 所有人物关系页面<br>
     |-KGQA.html 人物关系问答页面<br>
3)  raw_data 三元组数据<br>
5)  neo_db 知识图谱构建模块<br>
     |-config.py 配置参数<br>
     |-create_graph.py 建立图数据库<br>
     |-query_graph.py 知识图谱查询<br>
6)  KGQA 问答系统模块<br>
     |-ltp.py 分词、词性标注、命名实体识别<br>
7)  spider文件夹是爬虫模块<br>
     |- get_*.py 是之前爬取人物资料的代码，已经产生好images和json 可以不用再执行<br>
     |-show_profile.py 是调用人物资料和图谱展示在前端的代码
<hr>

部署步骤：<br>
* 0.安装所需的库 执行pip install -r requirement.txt<br>
* 1.先下载好neo4j图数据库，并配好环境（注意neo4j需要jdk8）。修改neo_db目录下的配置文件config.py,设置图数据库的账号和密码。<br>
* 2.切换到neo_db目录下，执行python  create_graph.py 建立知识图谱<br>
* 3.去 [这里](http://pyltp.readthedocs.io/zh_CN/latest/api.html#id2) 下载好ltp模型。[ltp简介](http://ltp.ai/)<br>
* 4.在KGQA目录下，修改ltp.py里的ltp模型文件的存放目录<br>
* 5.运行python app.py,浏览器打开localhost:5000即可查看<br>
