import re
import knock020

country = 'イギリス'
text = knock020.get_text(country)
sentences = text.strip().split('\n')

section_list = [sent for sent in sentences if sent.startswith('==')]
print('\n'.join([section+'\t'+str(int(section.count('=')/2-1)) for section in section_list]))
