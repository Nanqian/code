#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from xml.parsers.expat import ParserCreate


def fetch_WeatherXml():
    with request.urlopen(request.Request(
            'https://flash.weather.com.cn/wmaps/xml/beijing.xml')) as f:
        return f.read().decode('utf-8')


def parseXml(ele, attrs):
    try:
        print({
            'city': attrs['cityname'],
            'forecast': [
                {
                    'high': attrs['tem2'],
                    'low': attrs['tem1']
                },
            ]
        })
    finally:
        return


xml = fetch_WeatherXml()
parser = ParserCreate()
parser.StartElementHandler = parseXml
parser.Parse(xml)
