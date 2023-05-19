#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
p = {}
for line in sys.stdin:
    try:
        info = line.split(',')
        clr = info[33]
        if clr not in p:
            p[clr]=0
        p[clr] +=1
    except:
        pass

for index,row in p.items():
    print(str(index)+'\t'+str(row))
