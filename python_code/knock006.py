#!/usr/bin/python
# -*- coding: utf-8 -*-
import knock005
# 自分のコード
str1 = "paraparaparadise"
str2 = "paragraph"

X = knock005.char_ngram(2, str1)
Y = knock005.char_ngram(2, str2)

print X
print Y
