import re
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.replace(".", "")
ls = s.split()
dic = {}
for i in range(1, len(ls)+1):
    if(i in [1, 5, 6, 7, 8, 9, 15, 16, 19]):
        dic.update({ls[i-1][:1]:i})
    else:
        dic.update({ls[i-1][:2]:i})
print(dic)
for k, v in sorted(dic.items(), key=lambda x:x[1]):
    print(k, v)
