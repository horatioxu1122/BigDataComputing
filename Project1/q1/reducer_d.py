#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
sums = {}
peak = (-1,-1)
for line in sys.stdin:
    info = line.split('\t')
    loc = info[0]
    count = int(info[1])
    try:
	if loc not in sums:
		sums[loc] = 0
	sums[loc] += count
    except:
        pass

for loc,count in sums.items():
	if count > peak[1]:
		peak = (loc,count)

print(str(peak[0])+'\t'+str(peak[1]))

