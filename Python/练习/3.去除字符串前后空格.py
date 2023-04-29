#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def trim(s):
    # 检索第一个非空格字符的索引号
    i = 0
    for c in s:
        if c != ' ':
            break
        i += 1
    # 检索从后往前第一个非空格字符的索引号
    j = -1
    if s[i:] != '':
        while s[j] == ' ':
            j -= 1
    if j == -1:
        return s[i:]
    return s[i:j + 1]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


# 来自网友的更好的方案：
# def trim(s):
#
#     if s[:1]==' ':
#
#         return trim(s[1:])
#
#     elif s[-1:]==' ':
#
#         return trim(s[:-1])
#
#     else:
#
#         return s
