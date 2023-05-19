#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
p = {}
for line in sys.stdin:
    try:
        info = line.split(',')
        brand = info[7]
        year = int(info[35])
        if brand == '':
            continue
        if year == 0:
            continue
        if (brand,year) not in p:
            p[(brand,year)]=0
        p[(brand,year)]+=1
    except:
        pass

for index,row in p.items():
    print(str(index)+'\t'+str(row))
