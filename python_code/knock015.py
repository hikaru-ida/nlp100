#/usr/bin/python
# -*- coding: utf-8 -*-

import sys
input_file = open('../data/hightemp.txt', 'r')

n = input()
data = []
for line in input_file:
    data.append(line.strip())
l = len(data)

for i in range(l-n, l):
    print data[i]
