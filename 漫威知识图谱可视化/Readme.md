运行方式：
1. 配置环境以及安装neo4j，python版本需为3.6
2. 控制台输入 "neo4j console" 启动neo4j
3. 修改“KG_Marvel\neo_db\config.py”中的用户名密码
4. 解压“KG_Marvel\KGQA\ltp_data_v3.4.0.zip”
4. 修改“KG_Marvel\KGQA\ltp.py”中的模型路径（需用绝对路径）
4. 运行“KG_Marvel\neo_db\creat_graph.py”，将关系传入数据库
5. 运行  "KG_Marvel\app.py"
6. 浏览器输入“http://localhost:5000/”，进入知识图谱。

文件描述：
1. 存放爬虫文件
2. KGQA: 储存了基于ltp模型的分词函数
3. neo_db: 建立neo4j数据库
4. raw_data: 通过直接爬取得到的一些数据和数据预处理文件
5. spyder：储存超级英雄个人信息和图片以及关系
6. static: 网页中用到的图片字体等
7. templates: 网页脚本
8. app.py: 启动知识图谱