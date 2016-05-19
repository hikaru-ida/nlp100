#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
input_file = open('../data/hightemp.txt', 'r')

N = input()

n = N
for line in input_file:
    if n <= 0:
        break
    print line.strip()
    n = n - 1
    

input_file.close()
