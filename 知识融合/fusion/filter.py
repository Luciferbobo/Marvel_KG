# coding=utf-8
import json as json
import codecs
fusion=[]
f2= open('fusion.json',encoding='utf8')
fusion = json.load(f2)


baiduheros=["钢铁侠","美国队长","绿巨人","雷神","黑寡妇","战争机器","鹰眼","尼克弗瑞","猎鹰","幻视","绯红女巫","快银","奥创","特工希尔","斯特拉克男爵","特工卡特","海姆达尔","小辣椒","霍华德·史塔克","玛丽亚·斯塔克","奥巴代亚·斯坦尼","埃德温·贾维斯","菲尔·科尔森","鞭索二代","鞭索一代","贾斯汀·汉默","奥尔得雷齐·基里安","玛雅·汉森","憎恶","大头目","洛基","奥丁","弗丽嘉","希芙","沃斯塔格","霍根","范达尔","简·福斯特","达西·路易斯","劳菲","毁灭者","玛勒基斯","阿尔戈里姆","博尔","海拉","瓦尔基里","斯科尔奇","寇格","苏尔特尔","詹姆斯·布坎南·巴恩斯","达姆弹·杜根","切斯特·菲利普斯","亚伯拉罕·厄斯金","约翰·施密特","阿尼姆·佐拉","亚历山大·皮尔斯","交叉骨","莎朗·卡特","跳跃者巴托克","特查拉","特查卡","埃弗雷特·罗斯","赫尔穆特·泽莫","灭霸","星爵","卡魔拉","毁灭者德拉克斯","火箭浣熊","格鲁特","勇度","星云","罗南","齐塔瑞","收集者","黄蜂女","罗曼·戴","伊拉尼·雷尔","霍华德怪鸭","螳螂","伊戈","星辰鹰","银影侠","查理-27","蚁人","初代蚁人","黄蜂侠","奇异博士","莫度男爵","古一","卡西利亚斯","克里斯汀·帕尔默","王","乔纳森·斯威夫特","多玛姆","彼得·帕克","梅·帕克","内德·利兹","秃鹫","闪电·汤普森","徘徊者","赫尔曼·舒尔茨","修补匠","苏里","乌木喉","黑矮星","贝蒂·布兰特"]

for i in baiduheros:
    d['new_name'] = d.pop('old_name')
    for j in fusion[i].keys():
        print(j)