#!/usr/bin/env python

import sys

for line in sys.stdin:
	line = line.strip()
	hrIP, count = line.split('\t')
	hour, ip = hrIP.split(';')
	print('%s\t%s;%s' %(hour, ip, count))
