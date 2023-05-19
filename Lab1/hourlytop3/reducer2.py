#!/usr/bin/env python

from operator import itemgetter
from collections import defaultdict
import sys

dct_hour_ipcount = defaultdict(list)

for line in sys.stdin:
	line = line.strip()
	hour, ipcount = line.split('\t')
	ip, count =  ipcount.split(';')
	
	try:
		count = int(count)
		dct_hour_ipcount[hour].append([ip,count])
	except ValueError:
		pass

for hour in dct_hour_ipcount:
	dct_hour_ipcount[hour].sort(key = lambda x:x[1], reverse = True)
	dct_hour_ipcount[hour] = dct_hour_ipcount[hour][:3]
	for ip, count in dct_hour_ipcount[hour]:
		print('%s\t%s\t%s'%(hour, ip, count))
