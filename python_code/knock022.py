# -*-coding: utf-8 -*-
import re
import knock020

pattern = r'\[\[Category.*\]\]'
country = 'イギリス'
text = knock020.get_text(country)
texts = text.strip().split('\n')

repatter = re.compile(pattern)
match = []
for line in texts:
    matchOB = repatter.match(line)
    if matchOB:
        match.append(matchOB.group())

for i in range(len(match)):
    print (match[i])
