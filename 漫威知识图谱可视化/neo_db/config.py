from py2neo import Graph
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123"
)
CA_LIST = {"漫威宇宙":0}
similar_words = {
    "朋友":"朋友",
    "爱人":"爱人",
    "情人":"爱人",
    "恋人":"爱人",
    "共事":"共事",
    "同事":"共事",
    "敌人":"敌人",
    "家人":"家人"
}
