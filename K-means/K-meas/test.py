# -*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np

"""
    Pyplot tutorial  by kevinelstri 2017.3.3
"""
"""
    matplotlib.pyplot 是一个命令式的功能的集合使得matplotlib类似于MATLAB。
    每一个pyplot函数都使函数做一些改变：创建一个图形，创建一个绘图区域，在绘图区域绘制线，使用标签装饰图像等等。
"""
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.axis([0, 4, 0, 4])
plt.show()
"""
    x轴坐标从0到3，y轴坐标从1到4，但是图形是一条直线。
    当你提供一个简单的list或array作为plot命令，matplotlib假设这个序列是y值，并会自动分配x值。
    由于python序列式从0开始的，所以默认x向量的长度与y向量长度相等，并且是从0开始的，因此x=[0,1,2,3]
"""
# plt.plot(x,y)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # 'ro'表示使用圆圈来表示坐标，并且使用红色
plt.axis([0, 5, 0, 20])
plt.show()
"""
    axis([xmin, xmax, ymin, ymax]) 指定图像的大小，分别使用x轴范围和y轴范围进行限定
"""
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')  # 'r--'：red 虚线,'bs'：blue 正方形,'g^':green 三角形
plt.show()
"""
    Controlling line properties  控制线的属性
"""
x = [2, 3, 4, 5]
y = [1, 3, 5, 7]
plt.plot(x, y, linewidth=2.0)  # linewidth 表示线宽
plt.axis([1, 6, 0, 8])
plt.show()

line, = plt.plot(x, y, '-')
line.set_antialiased(False)
print(line)  # line线的方式
plt.axis([1, 6, 0, 8])
plt.show()

x1 = [2, 3, 4, 5]
y1 = [1, 3, 5, 7]
x2 = [1, 3, 4, 7]
y2 = [2, 3, 4, 5]
lines = plt.plot(x1, y1, x2, y2)
plt.setp(lines, color='r', linewidth=2.0)
# plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
plt.show()

lines = plt.plot([1, 2, 3])
print(plt.setp(lines))

"""
    working with multiple figures and axes 使用多种图形和坐标轴
"""
import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')  # 将两个图放在一起，一个为蓝色圆，一个为黑色线

plt.subplot(212)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')

plt.show()
print('---------------------------------------------')

import matplotlib.pyplot as plt

plt.figure(1)
plt.subplot(211)  # 图像展示，2行1列，第一行
plt.plot([1, 2, 3])
plt.subplot(212)  # 2行1列，第二行
plt.plot([4, 5, 6])

plt.figure(2)
plt.plot([4, 5, 6])

plt.figure(1)
plt.subplot(211)
plt.title('easy as 1, 2, 3')
"""
    working with text
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probaility')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
print('---------------------------------------------')

import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))
plt.ylim(-2, 2)
plt.show()
print('---------------------------------------------')
"""
    Logarithmic and other nonlinear axis 对数和其他非线性轴
"""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure(1)

# linear
plt.subplot(221)  # 2行2列，第1个
plt.plot(x, y)
plt.yscale('linear')  # 坐标的刻度
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)  # 2行2列，第2个
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)  # 2行2列，第3个
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)  # 2行2列，第4个
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()

"""
    matplotlib 常用api：
        1、plt.figure(num=None, figsize=(8,6), dpi=80, facecolor='w', edgecolor='k')
            figsize 图像大小，一般比例都在4：3
            facecolor 、edgecolor 分别表示图像颜色
        2、多行多列的subplots
            plt.subplot(221), plt.subplot(222), plt.subplot(223), plt.subplot(224)
        3、使用Latex
            $\sigma$ :以字符串形式，置于$$环境中；
            \ 有转义的意义：\ 出现的位置换成 \\,$\sigma$ -> $\\sigma$
        4、可选参数
            marker:'o'(圆形), 'x', '^'(三角形), 'v', 's'(方形)
            markersize/ms
            linestyle/ls:'-'(实线), '-.'(虚点), ':'(冒号), '--'(虚线)
            linewidth/lw
            color/c
            label
        5、常用api
            plt.xticks([]): 关闭坐标轴刻度，以tuple或者list为参数
            plt.yticks([])
            plt.axis('off'):关闭坐标轴
            plt.axis([x1,x2,y1,y1]) 坐标轴范围，x[x1,x2],y[y1,y2]
            plt.legend(loc={'best', 'upper left'},frameon=False): 图例的使用,默认是加框的
            plt.ylim():坐标轴的范围  x1_min,x1_max = x[:,0].min()-1,x[:,0].max()+1
            plt.xlim()：            x2_min,x2_max = x[:,1].min()-1,x[:,1].max()+1
            plt.yscale('log'):坐标的刻度
            plt.text():填写文本信息，前两个参数表示坐标，第三个参数对应文本信息
            plt.axhline():画水平线
            plt.axvline()：画垂直线

"""