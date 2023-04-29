#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HtmlParser是一个类，在使用时一般继承它然后重载它的方法，来达到解析出需要的数据的目的。
#
# 　　1.常用属性：
#
# 　　　　lasttag，保存上一个解析的标签名，是字符串。
#
# 　　2.常用方法：　
#
# 　　　　handle_starttag(tag, attrs) ，处理开始标签，比如<div>；这里的attrs获取到的是属性列表，属性以元组的方式展示
# 　　　　handle_endtag(tag) ，处理结束标签,比如</div>
# 　　　　handle_startendtag(tag, attrs) ，处理自己结束的标签，如<img />
# 　　　　handle_data(data) ，处理数据，标签之间的文本
# 　　　　handle_comment(data) ，处理注释，<!-- -->之间的文本

# 获取Python官网发布的会议时间、名称和地点

from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__parsedata = ''
        self.meeting = []

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__parsedata = 'name'
        if tag == 'time':
            self.__parsedata = 'time'
        if tag == 'span' and ('class', 'event-location') in attrs:
            self.__parsedata = 'location'

    def handle_data(self, data):
        if self.__parsedata == 'name':
            self.meeting.append(f'会议名称：{data}')
        if self.__parsedata == 'time':
            self.meeting.append(f'会议时间：{data}')
        if self.__parsedata == 'location':
            self.meeting.append(f'会议地点：{data}\n')

    def handle_endtag(self, tag):
        self.__parsedata = ''  # 在标签结束时，把标志位清空


def main():
    url = 'https://www.python.org/events/python-events/'
    req = request.Request(url)
    with request.urlopen(req) as f:
        data = f.read()

    parser = MyParser()
    parser.feed(data.decode('utf-8'))

    for info in parser.meeting:
        print(info)


if __name__ == '__main__':
    main()
