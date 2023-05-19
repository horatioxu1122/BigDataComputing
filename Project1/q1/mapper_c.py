#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
p = {}
for line in sys.stdin:
    try:
        info = line.split(',')
        zone = info[13].lstrip('0')
	if zone == '':
		continue
        if zone not in p:
            p[zone]=0
        p[zone] +=1
    except:
        pass

for index,row in p.items():
    print(str(index)+'\t'+str(row))
