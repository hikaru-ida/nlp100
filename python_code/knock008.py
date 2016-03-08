#!/usr/bin/python
# -*- coding: utf-8 -*-

#  自分のコード
def cipher(sent):
    my_sent = ""
    for i in range(len(sent)):
        if sent[i].islower():
            my_sent += chr(219 - ord(sent[i]))
        else:
            my_sent += sent[i]
            
    return my_sent

print cipher("abcABCdeDEFghijk")

# 他の人のコード
def _cipher(my_text):
    new_text = ""
    for char in my_text:
        if char.islower():
            char = chr(219 - ord(char))
        new_text += char
    return new_text

print _cipher("abcABCdeDEFghijk")
