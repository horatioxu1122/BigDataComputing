#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
pairs = {}
for line in sys.stdin:
    try:
        info = line.split(',')
        shooter = (info[15]+info[16]).strip('"')
        hit = info[14]
        defender = info[21]
        if (shooter,defender) not in pairs:
            pairs[(shooter,defender)] = [0,0]
        if hit == 'made':
            pairs[(shooter,defender)][0] +=1
        else:
            pairs[(shooter,defender)][1] +=1
    except:
        pass

for people,count in pairs.items():
    print(str(people)+"\t"+str(count))

