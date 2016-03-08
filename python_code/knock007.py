#!/usr/bin/python
# -*- coding: utf8 -*-

# 自分のコード
def xyz(x, y, z):
    return str(x) + "時の" + y + "は" + str(z)

print xyz(12,"気温", 22.4)

# 他の人のコード
def main(x, y, z):
    my_text = "%d時の%sは%f" %(x, y, z)
    return my_text

if __name__ == '__main__':
    x = 12
    y = "気温"
    z = 22.4
    print main(x, y, z)
