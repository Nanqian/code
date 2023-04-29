#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import uuid
import requests
import io
import time
import re
from PIL import Image

my_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}


def get_signParams():
    url = 'https://passport.baidu.com/v2/api/getqrcode?lp=pc&qrloginfrom=pc'
    html = requests.get(url, headers=my_header)
    signParams = html.json()['sign']
    return signParams


sign = get_signParams()
gid = str(uuid.uuid4()).upper()
bduss = ''

gc_flag = False


def get_qrcode():
    global gc_flag
    my_params = {
        'sign': sign,
        'lp': 'pc',
        'qrloginfrom': 'pc',
    }
    get_qrc_url = 'https://passport.baidu.com/v2/api/qrcode'
    html = requests.get(get_qrc_url, params=my_params, headers=my_header)
    with Image.open(io.BytesIO(html.content)) as qrcode:
        gc_flag = True
        qrcode.show()


def track_qrcStatus():
    global bduss
    while True:
        start_time = time.time()
        my_params = {
            'channel_id': sign,
            'gid': gid,
            'tpl': 'tb',
            '_sdkFrom': '1',
            'apiver': 'v3',
            'tt': time.time() * 1000,
            '_': time.time() * 1000,
        }
        qrcode_url = 'https://passport.baidu.com/channel/unicast'
        html = requests.get(qrcode_url, params=my_params,
                            headers=my_header).text
        html2 = html.replace('\\', '').replace('"{', "{").replace('}"',
                                                                  "}")
        message = json.loads(re.search(r'({.*})', html2).group())
        errno = message['errno']
        if errno == 0:
            status = message['channel_v']['status']
            if status == 0:
                bduss = message['channel_v']['v']
                break


def login():
    my_params = {
        'v': time.time() * 1000,
        'bduss': bduss,
        'u': '',
        'loginVersion': 'v4',
        'qrcode': 1,
        'tpl': 'tb',
        'apiver': 'v3',
        'tt': time.time() * 1000,
        'traceid': '',
        'time': time.time() * 1000,
        'alg': 'v3',
        'sig': 'QjhCUEJ0cmZnT1V0SnBOOVFKTW1wWHRja0gzQVlIdkpVRkZRRThmRVVPTGgyZ3dSdGVwTlZUR1AwRWlXZWFoUg==',
        'elapsed': 7,
        'shaOne': '006e00a3ba05331b6ef11441920e018323fe4a7f',
        'callback': 'bd__cbs__87q7g1'
    }
    login_url = 'https://passport.baidu.com/v3/login/main/qrbdusslogin'
    html = requests.get(login_url, params=my_params, headers=my_header)
    username = re.findall(r'"displayName": "(.*?)"', html.text)
    BDUSS = html.cookies['BDUSS']
    STOKEN = html.cookies['STOKEN']
    if len(username) > 0:
        print(f'用户：{username[0]}登录成功'.encode('utf-8'))
        time.sleep(1)
        with open('cookie.txt', 'w') as f:
            f.write(f'BDUSS={BDUSS};STOKEN={STOKEN};')
            print('成功在当前目录下生成cookie.txt')


def mian():
    if __name__ == '__main__':
        get_qrcode()
        if gc_flag:
            track_qrcStatus()
            login()
    time.sleep(1)
    input('按回车键退出程序...')


mian()
