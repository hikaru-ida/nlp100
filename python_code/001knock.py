#!/usr/bin/python
# -*- coding: utf-8 -*-

#自分のコード（一つ目）
print u"パタトクカシ――"[0:7:2].encode('utf-8')

#自分のコード（二つ目）
str1 = u"パタトクカシ――"
str2 = str1[0] + str1[2] + str1[4] + str1[6]

print str2.encode('utf-8')

#他の人のやつ
str_list = [str1[0], str1[2], str1[4], str1[6]]
print "".join(str_list).encode('utf-8')
