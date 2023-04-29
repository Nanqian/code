#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from turtle import undo

name_list = list()
undone_list = list()

with open('./名单.txt', 'r', encoding='utf-8') as f:
    if f == '':
        print('名单里还没有内容哦\n把人员填入名单后再来试试吧')
        input('\n\n按回车以结束...')
        exit()
    for line in f.readlines():
        name_list.append(line.strip())

inp = input("请将已接龙的名单粘贴到此处：")
done_list = []

while inp != '':
    names = re.findall(r'\d+\.\s([\u4E00-\u9FA5]{2,3})', inp)
    if len(names) > 1:
        done_list = names
        break
    done_list.append(names[0])
    inp = input()


def seek():
    for p in name_list:
        if p in done_list:
            continue
        else:
            undone_list.append(p)


def print_undone():
    if len(undone_list) != 0:
        print(u'\n\t未接龙的人有：')
        str = ''
        for p in undone_list:
            str  = str + '  ' + p
        print('\n\t%s' % str)
    else:
        print(u'\n\n\t太好啦！已全部完成接龙！')
    

def main():
    if __name__ == '__main__':
        seek()
        print_undone()
        input('\n\n按回车以结束...')


main()
