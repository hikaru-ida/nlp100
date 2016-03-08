#!/usr/bin/python
# -*- coding: utf-8 -*-

# 自分のコード
def char_ngram(n, sent):
    nchars = []
    for i in range(len(sent) - n + 1):
        nchars.append(sent[i: i+n])
    return nchars

def word_ngram(n, sent):
    words = ["<s>"] + sent.split()
    words.append("</s>")
    nwords = []
    for i in range(len(words) - n + 1):
        nwords.append(words[i: i+n])
    return nwords

str1 = "I am an NLPer"
print char_ngram(2, str1)
print word_ngram(2, str1)

# 他の人のコード
def word_ngram_(my_sent, n):
	words_bi_list = []
	words = ["<s>"] + my_sent.split()
	words.append("</s>")
	for i in range( len(words) - n + 1 ):
		words_bi_list.append(words[i: i + n])
	return words_bi_list


def char_ngram_(my_sent, n):
	char_bi_list = []
	for i in range(len(my_sent) - n + 1):
		if my_sent[i] == "" or my_sent[i+1] == " ": continue
		char_bi_list.append(my_sent[i: i+n])
	return char_bi_list
	
