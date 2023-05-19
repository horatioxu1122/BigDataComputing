#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
pairs = {}
for line in sys.stdin:
    pair,hit = line.split('\t')
    hit=eval(hit)
    people = pair.strip('(').strip(')').strip(' ').split(',')
    shoot = people[1]
    defend = people[0]
    if shoot not in pairs:
        pairs[shoot] = {}
    if defend not in pairs[shoot]:
        pairs[shoot][defend] = [0,0]
    pairs[shoot][defend][0] += hit[0]
    pairs[shoot][defend][1] += hit[1]


for person,item in pairs.items():
    for defend,scores in item.items():
         pairs[person][defend] = [(float(pairs[person][defend][1])/sum(pairs[person][defend])),sum(pairs[person][defend])]

for person,item in pairs.items():
    pairs[person] = sorted(pairs[person].items(), key = lambda x:(x[1][0]),reverse=True)

for person,item in pairs.items():
    for person2,item2 in item:
        if item2[1] < 5:
            continue
        print("{}\t{}".format((person,person2),item2))

