#!/usr/bin/python
# ---- coding:utf-8 ----
import random
import sys
cntd = 4
p = {}
cntds = {}

for line in sys.stdin:
    line = line.split('\t')
    player = line[0]
    data = eval(line[1])
    if player not in p:
        p[player] = []
    p[player].extend(data)

    
def l2(set1,set2):
    d=0
    for i in range(len(set1)):
        d+=(set1[i]-set2[i])**2
    return(d**0.5)

for player,data in p.items():
    if len(data) < 4:
        continue
    # Initialize centroids 
    if player not in cntds:
        cntds[player]=[]
    if not cntds[player]:
        nums = []
        for _ in range(cntd):
            nums.append(random.randint(0,len(data)-1))
            if len(nums)==1:
                continue
            while nums[-1] == nums[-2]:
                nums[-1] = random.randint(0,len(data)-1)
        for i in nums:
            cntds[player].append(data[i])
    # calc closest distances
    for _ in range(10):
        future_centroid = []
        for k in range(cntd):
            future_centroid.append([])
        for dataset in data:
            distances = []
            for centroid_positions in cntds[player]:
                dst = l2(centroid_positions,dataset)
                distances.append(dst)
            min_indx = -1
            min_val = 100000
            j=0
            for k in distances:
                if k < min_val:
                    min_val = k
                    min_indx = j
                j+=1
            future_centroid[min_indx].append(dataset)
        for ix,f_cntd in enumerate(future_centroid):
            d = []
            t=0
            try:
                for t in range(len(f_cntd[0])):
                    d.append(0)
                for row in f_cntd:
                    for k,point in enumerate(row):
                        d[k] += point
                    t +=1
                for indx,point in enumerate(d):
                    d[indx] = round(d[indx]/t,4)
                future_centroid[ix] = d
            except:
                pass
        for i in range(len(cntds[player])):
            if future_centroid[i]:
                cntds[player][i] = future_centroid[i]

for player,centroid_pos in cntds.items():
    print(player+'\t'+str(centroid_pos))

