#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def findMinAndMax(L):
    if L == []:
        return (None, None)
    maxNum = minNum = L[0]
    for value in L:
        if minNum > value:
            minNum = value
        if maxNum < value:
            maxNum = value
    return (minNum, maxNum)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')