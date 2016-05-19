#/usr/bin/python
# -*- coding: utf-8 -*-

input_file = open('../data/hightemp.txt', 'r')

data = []
for line in input_file:
    row = line.strip().split('\t')
    data.append(row)

data.sort(key=lambda x:x[2],reverse=True)

for i in range(len(data)):
    print '\t'.join(data[i])



