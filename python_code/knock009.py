#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

my_sent = "I couldn't believe that I could actually understand \
what I was reading : the phenomenal power of the human mind ."

# 自分のコード
words = my_sent.split(" ")
new_words = []
for i in range(len(words)):
    word = words[i]
    if len(words[i]) > 4: 
        middle = list(word[1:-1])
        random.shuffle(middle)
        word = word[0]+"".join(middle)+word[-1]
    new_words.append(word)

print " ".join(new_words)
