# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

# 读取文件
name = [[],[],[],[],[]]
with open('seconddata.txt') as f:
    for line in f:
        for each in enumerate(line.split()):
            name[each[0]].append(float(each[1]))
x,k3,k4,k5,k6= name
print(x)
print(k3)
print(k4)
print(k5)
print(k6)
#折线图
# plt.plot(x,k1,'s-',color = 'r',label="k=4")#s-:方形
# plt.plot(x,k2,'o-',color = 'g',label="k=4")#o-:圆形
plt.plot(x,k3,'s-',color = 'r',label="k=3")#s-:方形
plt.plot(x,k4,'o-',color = 'g',label="k=4")#o-:圆形
plt.plot(x,k5,'p-',color = 'b',label="k=5")
plt.plot(x,k6,'d-',color = 'k',label="k=6")#d-:钻石形

plt.xlabel("CircleTimes")#横坐标名字
plt.ylabel("SSE")#纵坐标名字
plt.title("k-SSE")
plt.legend(loc = "best")#图例
plt.show()