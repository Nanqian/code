#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta, timezone


# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
def to_timestamp(dt_str, utc_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    utc = int(re.match(r'\w+([\+\-]\d+):\d+', utc_str).group(1))
    dt = dt.replace(tzinfo=timezone(timedelta(hours=utc)))
    return dt.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
