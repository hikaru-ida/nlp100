#!/usr/bin/python
# -*- coding: utf-8 -*-
import knock005
# 自分のコード
str1 = "paraparaparadise"
str2 = "paragraph"

X = set(knock005.char_ngram(2, str1))
Y = set(knock005.char_ngram(2, str2))

print "和集合 -> "
print X.union(Y)
print "積集合 -> "
print X.intersection(Y)
print "差集合(X - Y) -> "
print X.difference(Y)
print "差集合(Y - X) -> "
print Y.difference(X)

if "se" in X:
    print "seはXに含まれる"
else:
    print "seはXに含まれない"


if "se" in Y:
    print "seはYに含まれる"
else:
    print "seはYに含まれない"
