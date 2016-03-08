#!/usr/bin/python
# -*- coding: utf-8 -*-

#自分のコード
str1 = u"パトカー"
str2 = u"タクシー"
str3 = u""
for i in range(len(str1)):
    str3 += str1[i] + str2[i]

print str3.encode('utf-8')

#他の人のコード
s = ""
for i, j in zip(str1, str2):
    s+= i + j

print s.encode('utf-8')
