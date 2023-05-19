#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
p = {}
pairs = {}
clustrs = sys.argv[1].split('\n')
clustrs = [eval(x.split('\t')[0]) for x in clustrs]

def l2(x1,x2):
    td = 0
    for i in range(len(x1)):
        td += (x2[i]-x1[i])**2
    return td**0.5

def closest(point,clusters,taken):
    peak = 0
    m_d = 100000000
    p_point = -1
    for cluster in clusters:
        z=abs(point-cluster)
        if z < m_d and peak not in taken:
            m_d = z 
            p_point = peak
        peak += 1
    return p_point

for line in sys.stdin:
    try:
        info = line.split(',')
        zone = info[9:12]
        zone = [int(x) for x in zone]
        if 0 in zone:
            continue
        if info[33] != 'BLK':
            continue
    except:
        continue
    max_d = 10000000000
    best_clstr = -1
    k=0
    for clstr in clustrs:
        zone_reorg = [0 for _ in zone]
        tkn = []
        for point in zone:
            temp_clstr = clstr
            indx_closest = closest(point,temp_clstr,tkn)
            zone_reorg[indx_closest] = point
            tkn.append(indx_closest)
        dist = l2(zone_reorg,clstr)
        if dist < max_d:
            best_clstr = k
            max_d = dist
        k+=1
    if str(clustrs[best_clstr]) not in pairs:
        pairs[str(clustrs[best_clstr])] = []
    pairs[str(clustrs[best_clstr])].append(zone)

for key,item in pairs.items():
    print(str(key)+'\t'+str(item))
