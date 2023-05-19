#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for i in range(0,len(words)-1):
        if i > 0:
            print "%s %s\t%s" % (words[i-1],words[i], 1)
