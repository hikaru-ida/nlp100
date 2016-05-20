#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import Counter

input_file = open('../data/hightemp.txt', 'r')

data = []
for line in input_file:
    data.append(line.strip().split('\t')[0])

cnt = Counter()
for word in data:
    cnt[word] += 1

for items in cnt.most_common():
    print '%d %s' % (items[1], items[0])

