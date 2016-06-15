# -*- coding: utf-8 -*-
import knock020

country = 'イギリス' 
text = knock020.get_text(country)
texts = text.split('\n')

for line in texts:
    if 'Category' in line:
        print (line)

