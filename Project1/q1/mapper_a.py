#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
p = {}
for line in sys.stdin:
    try:
        info = line.split(',')
        time = info[19]
        if time[4].lower() is 'p':
            time = 12+int(time[:2])
        else:
            time = int(time[:2])
        if time >24:
            continue
        if time not in p:
            p[time]=0
        p[time] +=1
    except:
        pass

for index,row in p.items():
    print(str(index)+'\t'+str(row))
