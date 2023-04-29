#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


def allDir():
    for x in os.listdir('.'):
        print(x)


def seek():
    path = input('Please input a path：\n\t')
    fname = input('Please input a key-word of the file：\n\t')

    for x in os.listdir(path):
        if fname in x:
            print('%s，其绝对路径为\"%s\"' % (x, os.path.abspath(x)))


seek()
