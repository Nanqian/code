#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re


# 版本一可以验证出类似的Email：
#   someone@gmail.com
#   bill.gates@microsoft.com


def is_valid_email(adr):
    re_email = re.compile(r'^\w+\.?\w+(@)\w+\.\w+?$')
    if re_email.match(adr):
        return True
    else:
        return False


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


# 版本二可以提取出带名字的Email地址：
#   <Tom Paris> tom@voyager.org => Tom Paris
#   bob@example.com => bob


def name_of_email(adr):
    result = re.match(r'^<?(\w+\s?\w+)>?.*(@)(\w+\.\w+?)$', adr)
    if result:
        return result.group(1)


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
