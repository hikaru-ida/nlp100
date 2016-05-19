#/usr/bin/python
# -*- coding: utf-8 -*-

input_file = open('../data/hightemp.txt', 'r')

set_col1 = set([])
for line in input_file:
    set_col1.add(line.split('\t')[0])

for col1 in set_col1:
    print col1
