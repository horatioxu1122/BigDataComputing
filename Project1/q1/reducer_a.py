#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
sums = {}
peak = (-1,-1)
for line in sys.stdin:
    info = line.split('\t')
    time = int(info[0])
    count = int(info[1])
    try:
	if time not in sums:
		sums[time] = 0
	sums[time] += count
    except:
        pass

for time,count in sums.items():
	if count > peak[1]:
		peak = (time,count)

print(str(peak[0])+'\t'+str(peak[1]))

