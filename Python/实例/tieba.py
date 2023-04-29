#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import os
import time
import platform
from bs4 import BeautifulSoup

my_cookie = 'BIDUPSID=D313BE28C272E5B08EBC2161868E0F7B; PSTM=1658384393; newlogin=1; BDUSS=hndll-RWR1bnNWUkNnbXNtM2REcmFqYk9PdmNIZWkyZ1FwYXlFZ0dVeHVoQUJqRVFBQUFBJCQAAAAAAAAAAAEAAADTSJskQ1hYi5-NrwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG732GJu99hiS3; BDUSS_BFESS=hndll-RWR1bnNWUkNnbXNtM2REcmFqYk9PdmNIZWkyZ1FwYXlFZ0dVeHVoQUJqRVFBQUFBJCQAAAAAAAAAAAEAAADTSJskQ1hYi5-NrwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG732GJu99hiS3; STOKEN=6559548580fdb2b1d0f4ee47590df340f27e968d8167770b6900cd7b8cee5798; BAIDUID=D313BE28C272E5B08EBC2161868E0F7B:SL=0:NR=10:FG=1; ZFY=HNxvEtE2dBNBdgQNRj3AtJT8mprdnOmXFDu5R6rQbdw:C; BAIDU_WISE_UID=wapp_1660576368680_877; BAIDUID_BFESS=D313BE28C272E5B08EBC2161868E0F7B:SL=0:NR=10:FG=1; rpln_guide=1; USER_JUMP=-1; RT="z=1&dm=baidu.com&si=84fdb9e7-5087-4a79-944e-c130f6c393ff&ss=l70azxzg&sl=2&tt=1q2&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&r=2baynwak&hd=5hdu"; 614156499_FRSVideoUploadTip=1; video_bubble614156499=1; showCardBeforeSign=1'
my_header = {'Cookie': my_cookie,
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}


def clear():
    # 返回系统平台/OS的名称，如Linux，Windows，Java，Darwin
    system = platform.system()
    if system == u'Windows':
        os.system('cls')
    else:
        os.system('clear')


def get_tbs(kw):
    res_s = requests.get(f'https://tieba.baidu.com/f?kw={kw}',
                         headers=my_header)
    soup_s = BeautifulSoup(res_s.text, 'lxml')
    sc = soup_s.find_all('script')[1]
    tbs = re.search(r'\'tbs\': "(.*?)"', str(sc))
    return tbs.group(1)


success_num = 0
repeat_sign = 0


def signup(tb):
    global success_num, repeat_sign
    print(f' \n ♪{tb}吧')
    tb_data = {
        'ie': 'utf-8',
        'kw': tb,
        'tbs': get_tbs(tb),
    }
    req = requests.post('https://tieba.baidu.com/sign/add', data=tb_data,
                        headers=my_header)
    if req.json()['error'] == '':
        success_num += 1
        print(u'   签到成功')
    elif req.json()['error'] == u'亲，你之前已经签过了':
        repeat_sign += 1
        print(u'   已经签过了啦')
    else:
        print(u'   遭遇不明力量袭击，签到失败！')
    time.sleep(1)


def autoSignup():
    res = requests.get('https://tieba.baidu.com/f/like/mylike',
                       headers=my_header)
    tb_list = re.findall(r'<a href=".*?" title=".*?">(.*?)</a>', res.text)
    print(f'\n\n\n您有{len(tb_list)}个吧待签到')
    print('----------------')
    for tb in tb_list:
        signup(tb)
    fail_num = len(tb_list) - success_num - repeat_sign
    print('----------------')
    print(
        f'您本次尝试签到{len(tb_list)}个吧，其中：\n'
        f'    {success_num}个签到成功，{repeat_sign}个已经签到过，{fail_num}个签到失败')
    print(u'\n\n所有贴吧签到完成，感谢您的使用！')


def main():
    if __name__ == '__main__':
        clear()
        for t in range(0, 5):
            print(
                u'\t\n-- 该文件仅用于学习交流，请合法使用并在下载后的24小时内删除！ --\n')
            time.sleep(0.3)
        time.sleep(1.5)
        clear()
        if my_cookie == '':
            print(u'似乎有什么东西遗漏了哦')
            return
        autoSignup()
    input(u'按任意键关闭程序…')


main()
