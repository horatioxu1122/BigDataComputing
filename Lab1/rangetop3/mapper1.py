#!/usr/bin/python
# --*-- coding:utf-8 --*--

import re
import sys


start, end = sys.argv[1].split('-')
hour_range = range(int(start), int(end)+1)

pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*?')

for line in sys.stdin:
	match = pat.search(line)
	if match and (int(match.group('hour')) in hour_range):
		print("%s\t%s" % (match.group('ip'), 1))
