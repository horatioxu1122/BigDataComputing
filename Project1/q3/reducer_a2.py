#!/usr/bin/python
# ---- coding:utf-8 ----
import sys
p = {}
g=[]

def list_division(lst,num):
    new_lst = []
    for k in lst:
        new_lst.append(round(k/num,4))
    return new_lst

for line in sys.stdin:
    try:
        info = line.split('\t')
        cluster = info[0]
        points = eval(info[1])
        if cluster not in p:
            p[cluster] = []
        p[cluster].extend(points)
    except:
        pass
    
new_clusters = []
tots = []
for cluster,dataset in p.items():
    count = len(dataset)
    sums = [0 for _ in range(len(dataset[0]))]
    for sets in dataset:
        for i,point in enumerate(sets):
            sums[i] += point
    new_clusters.append(list_division(sums,count))
    tots.append(count)

for k in range(len(new_clusters)):
    print(str(new_clusters[k])+'\t'+str(tots[k]))
