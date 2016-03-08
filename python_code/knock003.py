#!/usr/bin/python
# -*- coding: utf-8 -*-

# 自分のコード
str1 = '''Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'''
words = str1.replace(",", "").replace(".", "").split(" ")
word_len = []
for word in words:
    word_len.append(len(word))
print word_len

# 他の人のコード
my_sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words_len = []
words = my_sent.split()
for word in words:
    if word.endswith(',') or word.endswith('.'):
        word = word[:-1]
    words_len.append(len(word))

print words_len

