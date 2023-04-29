#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import json


def fetch_data(url):
    with request.urlopen(url) as f:
        return json.loads(f.read().decode('utf-8'))


# 测试
URL = 'https://www.httpbin.org/get'
data = fetch_data(URL)
print(data)
print('ok')
