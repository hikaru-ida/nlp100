import knock020
import re

text = knock020.get_text('イギリス')

def get_kisojoho(country_text):
    pattern = r'^\|.*\s=\s.*'
    repatter = re.compile(pattern)
    items = text.strip().split('\n')
    info_dic = {}
    for item in items:
        if repatter.match(item):
            item = item.replace('|','')
            key , value = item.split(' = ')
            info_dic[key] = value
    return info_dic

if __name__ == '__main__':
    dic = get_kisojoho(text)
    for k, v in dic.items():
        print(k+'\t'+v)

