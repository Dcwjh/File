# -*- coding:utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
WS = nx.random_graphs.watts_strogatz_graph(100,4,0.04)  #生成包含20个节点、每个节点4个近邻、随机化重连概率为0.3的小世界网络
pos = nx.random_layout(WS)          #定义一个布局，此处采用了circular布局方式
nx.draw(WS,pos,with_labels=False,node_size = 30)  #绘制图形
plt.show()
sum = 0
j = 0
for i in WS.degree:
    sum = sum + i[1]
print(sum/len(WS.degree))
print(nx.average_clustering(WS))