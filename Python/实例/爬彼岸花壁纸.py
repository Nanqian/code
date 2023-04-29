import requests
import os, re, time


# 创建文件夹
def file_folder():
    # 创建mydata文件夹
    # 如果mydata文件夹已存在，清空文件夹(先清空后删除再创建)
    pathd = os.getcwd() + '\\彼岸花4k壁纸'
    if os.path.exists(pathd):
        for root, dirs, files in os.walk(pathd, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))  # 删除文件
            for name in dirs:
                os.remove(os.path.join(root, name))  # 删除文件夹
        os.rmdir(pathd)  # 删除mydaata文件夹
    os.mkdir(pathd)  # 创建mydata文件夹


count_1 = 1


def data(url):
    if re.search(r'/index_1.html', url):
        url = url.replace('index_1.html', 'index.html')
    res = requests.get(url)
    res.encoding = 'gbk'
    res = res.text
    url_r = '<li><a href="(.*?)" target="_blank"><img.*?><b>.*?</b></a></li>'
    url_name = re.findall(url_r, res)
    for p in url_name:
        global count_1
        res_s = requests.get('https://pic.netbian.com' + p)
        res_s.encoding = 'gbk'
        res = res_s.text
        r = '<div class="photo-pic"><a href="" id="img"><img src="(.*?)".*?></a></div>'
        url_list = re.findall(r, res)
        print(url_list)
        if len(url_list) == 0:
            continue
        pic_url = 'https://pic.netbian.com' + url_list[0]
        res = requests.get(pic_url)
        with open(f'{os.getcwd()}\\彼岸花4k壁纸\\{count_1}.jpg', 'wb') as f:
            f.write(res.content)
        count_1 += 1
        time.sleep(1.5)


if __name__ == '__main__':
    types = {'1':'4kfengjing','2':'4kmeinv','3':'4kyouxi','4':'4kdongman','5':'4kyingshi','6':'4kqiche','7':'4kdongwu','8':'4krenwu','9':'4kmeishi','10':'4kzongjiao','11':'4kbeijing','12':'shoujibizhi'}
    type = input(
        '图片网站：https://pic.netbian.com\n文件保存在彼岸花4k壁纸文件夹里\n请输入爬取的类型\n'
        '\n1.风景 2.美女 3.游戏 4.动漫 5.影视 6.汽车 7.动物 8.人物 9.美食 10.宗教 11.背景 12.手机壁纸\n'
        '请选择类型：')
    url = f'https://pic.netbian.com/{types[type]}/index_'
    pageStart = input('请输入开始页数：')
    pageStop = input('请输入结束页数：')
    file_folder()
    for i in range(int(pageStart), int(pageStop)+1):
        st = url + str(i) + '.html'
        print(f'开始爬取第{i}页')
        data(st)
        print(f'第{i}页爬取完毕')
    print('\n---如果文件夹不加载图片说明网址输入错误---\n')