#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
p = {}
for line in sys.stdin:
    try:
        info = line.split(',')
        shooter = (info[15]+info[16]).strip('"')
        hit = info[14]
        def_dist = float(info[18])
        time = float(info[9])
        dist = float(info[12])
        if shooter not in p:
            p[shooter] = []
        if hit == 'made':
            p[shooter].append((dist,def_dist,time))
    except:
        pass

for shooter,info in p.items():
    print(shooter+'\t'+str(info))

