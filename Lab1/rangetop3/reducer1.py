#!/usr/bin/python

import sys

dict_ip_count = {}

for line in sys.stdin:
	line = line.strip()
	ip, num = line.split('\t')

	try:
		num = int(num)
		dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num
	except ValueError:
		pass

for ip, count in dict_ip_count.items():
	print('%s\t%s' % (ip, count))
