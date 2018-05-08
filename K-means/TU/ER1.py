# -*- coding:utf-8 -*-

# ER模型50节点，连接概率p = 0.1
import networkx as ne #导入建网络模型包，命名ne
import matplotlib.pyplot as plt #导入科学绘图包，命名mp
#erdos renyi graphy
rg=ne.erdos_renyi_graph(50,0.1)
ps=ne.random_layout(rg)#布置框架
ne.draw(rg,ps,with_labels=False,node_size=30)
plt.xlabel("")#横坐标名字
plt.ylabel("")#纵坐标名字
plt.title("ER")
plt.show()
sum = 0
j = 0
for i in rg.degree:
    sum = sum + i[1]
print(sum/len(rg.degree))
print(ne.average_clustering(rg))
