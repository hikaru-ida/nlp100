#!/usr/bin/python
# -*_ coding: utf-8 -*-

import sys
input_file = open(sys.argv[1], 'r')
col1 = open('../data/col1.txt', 'w')
col2 = open('../data/col2.txt', 'w')

for line in input_file:
    line = line.strip()
    items = line.split('\t')
    [item1, item2] = [items[0], items[1]]
    col1.write(item1+'\n')
    col2.write(item2+'\n')

col1.close()
col2.close()

