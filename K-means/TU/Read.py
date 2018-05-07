# -*- coding:utf-8 -*-

name = [[],[],[],[],[]]
with open('firstdata.txt') as f:
    for line in f:
        for each in enumerate(line.split()):
            name[each[0]].append(float(each[1]))
a,b,e,c,d= name
print(a)
print(b)

print(c)
print(d)
print(e)
