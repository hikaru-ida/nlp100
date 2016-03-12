#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
input_file = open(sys.argv[1], "r")

for line in input_file:
    line = line.replace("\t", "\n")
    sys.stdout.write(line)

