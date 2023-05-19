#!/usr/bin/env python

import sys

for line in sys.stdin:
	line = line.strip()
	ip, count = line.split("\t")
	print('%s\t%s'%(count, ip))
