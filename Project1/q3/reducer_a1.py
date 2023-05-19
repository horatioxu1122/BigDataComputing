#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
import random
p = {}
g=[0]
centroids = 1
for line in sys.stdin:
    try:
        info = line.split('\t')
        g[0]=eval(info[0])
    except:
        pass

centrds = random.sample(g,centroids)

for cn in centrds:
        print(str(cn)+'\t1')
