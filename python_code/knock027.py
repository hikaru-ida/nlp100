import knock020
import knock026
import knock025

def remove_link(info_dic):
    dic = {}
    for k, v in info_dic.items():
        dic[k] = v.replace('[[','').replace(']]','')
    return dic

if __name__ == '__main__':
    text = knock020.get_text('イギリス')
    info_dic = knock025.get_kisojoho(text)
    knock026.remove_emphasis(info_dic)
    dic = remove_link(info_dic)
    for k, v in dic.items():
        print(v)
