#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一个: 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
from functools import reduce


def normalize(name):
    return name.capitalize()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
if L2 == ['Adam', 'Lisa', 'Bart']:
    print('第一个测试成功！')
else:
    print('第一个测试失败！')


# 第二个: 接受一个list并求乘积
def prod(L):
    def multiplication(x, y):
        return x * y

    return reduce(multiplication, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('第二个测试成功!')
else:
    print('第二个测试失败!')


# 第三个: 把字符串转换成浮点数
def str2float(s):
    def char2num(c):
        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return DIGITS[c]

    # 处理小数点前
    s1 = s
    while s1[-1] != '.':
        s1 = s1[:-1]
    s1 = s1[:-1]

    def fn1(x, y):
        return x * 10 + y

    # 处理小数点后
    s2 = s
    while s2[0] != '.':
        s2 = s2[1:]
    s2 = s2[1:]

    def fn2(num):
        n = 1
        for i in s2:
            n = n * 10
        return num / n

    f1 = reduce(fn1, map(char2num, s1))
    f2 = fn2(reduce(fn1, map(char2num, s2)))

    return f1 + f2


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('第三个测试成功!')
else:
    print('第三个测试失败!')
