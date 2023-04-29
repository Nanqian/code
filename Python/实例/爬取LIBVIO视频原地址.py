#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

my_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
session = requests.session()


# 获取视频地址
def get_vdURL():
    pg_url = 'https://www.libvio.me/play/699-1-1.html'
    req = session.get(pg_url, headers=my_header)
    soup = BeautifulSoup(req.text, 'lxml')
    tag = soup.select('.dplayer-video')
    print(soup)


get_vdURL()
