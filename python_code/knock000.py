# -*- coding: utf-8 -*-

#自分のコード
sentence = "stressed"
str1 = ""
for i in range(len(sentence)):
    str1 += sentence[len(sentence) - i - 1]
print (str1)

#他の人のやつ
print (sentence[::-1])




