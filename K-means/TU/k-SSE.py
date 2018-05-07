# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

# 读取文件
name = [[],[]]
with open('data.txt') as f:
    for line in f:
        for each in enumerate(line.split()):
            name[each[0]].append(float(each[1]))
x,SSE = name
print(x)
print(SSE)
#折线图

plt.plot(x,SSE,'o-',color = 'k')#o-:圆形
plt.xlabel("k")#横坐标名字
plt.ylabel("SSE")#纵坐标名字
plt.title("k-SSE")
plt.legend(loc = "best")#图例
plt.show()