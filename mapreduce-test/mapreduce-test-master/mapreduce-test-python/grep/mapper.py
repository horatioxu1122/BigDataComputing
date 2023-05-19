#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys
if len(sys.argv) < 2:
    print "Pattern not found"
    sys.exit()
pat = re.compile(sys.argv[1])
for line in sys.stdin:
    match = pat.search(line)
    if match:
        print '%s\t%s' % ("input", 1)

