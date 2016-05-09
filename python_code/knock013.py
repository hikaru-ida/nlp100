#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

merge = open('../data/merge.txt', 'w')
col1 = open('../data/col1.txt')
col2 = open('../data/col2.txt')

lst1 = []
lst2 = []
for line in col1:
    lst1.append(line.strip())

for line in col2:
    lst2.append(line.strip())

for i in range(len(lst1) if len(lst1) > len(lst2) else len(lst2)):
    merge.write(lst1[i]+'\t'+lst2[i]+'\n')

merge.close()
