#!/usr/bin/python
# -*- coding: utf-8 -*-

# 自分のコード
def char_ngram(n, sent):
    nchars = []
    for i in range(len(sent) - n + 1):
        nchars.append(sent[i: i+n])
    return nchars

def word_ngram(n, sent):
    words = sent.split(" ")
    nwords = []
    for i in range(len(words) - n + 1):
        nwords.append(words[i: i+n])
    return nwords

str1 = "I am an NLPer"
print char_ngram(2, str1)
print word_ngram(2, str1)
# 
