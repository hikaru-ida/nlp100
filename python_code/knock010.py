#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

input_file = open(sys.argv[1], "r")
cnt = 0
for line in input_file:
    cnt += 1

print cnt
