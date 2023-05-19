#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
peak = (-1,-1)
sums = {}
for line in sys.stdin:
    info = line.split('\t')
    pair = info[0]
    count = int(info[1])
    try:
        if pair not in sums:
            sums[pair]=0
        sums[pair]+=count
    except:
        pass

for pair,count in sums.items():
    if count>peak[1]:
        peak = (pair,count)

print(str(peak[0])+"\t"+str(peak[1]))
