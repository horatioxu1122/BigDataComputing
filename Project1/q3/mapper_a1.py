#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
import random
p = {}
for line in sys.stdin:
    try:
        info = line.split(',')
        zone = info[9:12]
        zone = [int(x) for x in zone]
        if 0 in zone:
            continue
	print(str(zone)+'\t1')
    except:
        pass

