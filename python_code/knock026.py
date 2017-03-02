import knock020
import knock025
import re



def remove_emphasis(info_dic):
    for k, v in info_dic.items():
        info_dic[k] = v.replace("'''","")

if __name__ == '__main__':
    text = knock020.get_text('イギリス')
    info_dic = knock025.get_kisojoho(text)
    remove_emphasis(info_dic)
    for k, v in info_dic.items():
        print(v)

