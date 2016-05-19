#/usr/bin/python
# -*- coding: utf-8 -*-
import math

input_file = open('../data/hightemp.txt', 'r')

N = input()
data = []
divided = []

for line in input_file:
    data.append(line.strip())
cnt = len(data)/N

for i in range(0, len(data), N):
    if len(data)<N+i:
        divided.append(data[i:])
    else:
        divided.append(data[i:i+N])


for i in range(len(divided)):
    f = open('../data/%s.%02d' % ('divided', i) ,'w')
    f.write('\n'.join(divided[i])+'\n')
    f.close()
    
