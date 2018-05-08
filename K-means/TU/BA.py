# -*- coding:utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
BA= nx.random_graphs.barabasi_albert_graph(500,2)  #生成n=20、m=1的BA无标度网络
pos = nx.spring_layout(BA)          #定义一个布局，此处采用了spring布局方式
nx.draw(BA,pos,with_labels=False,node_size = 30)  #绘制图形
plt.show()
sum = 0
j = 0
for i in BA.degree:
    sum = sum + i[1]
print(sum/len(BA.degree))
print(nx.average_clustering(BA))
