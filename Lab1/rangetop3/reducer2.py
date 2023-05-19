#!/usr/bin/env python

import sys

for line in sys.stdin:
	line = line.strip()
	count, ip = line.split('\t')
	print('%s\t%s'%(ip, count))
