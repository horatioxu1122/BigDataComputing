#!/usr/bin/python
from operator import itemgetter
import sys

dict_word_count = {}

for line in sys.stdin:
    line = line.strip()
    word, num = line.split('\t')
    try:
        num = int(num)
        dict_word_count[word] = dict_word_count.get(word, 0) + num

    except ValueError:
        pass

sorted_dict_word_count = sorted(dict_word_count.items(), key=itemgetter(0))
for word, count in sorted_dict_word_count:
    print '%s\t%s' % (word, count)
