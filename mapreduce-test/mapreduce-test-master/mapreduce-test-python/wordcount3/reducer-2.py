#!/usr/bin/env python
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    frequency, word = line.split('\t', 1)
    print "%s\t%s" % (frequency, word)
