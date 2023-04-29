#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def quadratic(a, b, c):
    # 判断输入的是非为数字
    if not (isinstance(a, (int, float))
            and isinstance(b, (int, float))
            and isinstance(c, (int, float))):
        raise TypeError('bad operand type')
    # 若为一元一次函数
    if a == 0:
        x = -c / b
        return x
    # 判断delta
    delta = b**2 - 4 * a * c
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
    elif delta < 0:
        pass
    return x1, x2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
