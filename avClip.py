# -*- coding: utf-8 -*-
#!/usr/bin/env python
import webbrowser
import pyperclip
import time
import re


def sear(regexp, urlpref, message):
    rematch = re.findall(regexp, input)
    for item in rematch:
        url = urlpref + item
        print(u'检测到 ' + message + u': ' + url)
        webbrowser.open_new_tab(url)


prevclip = ''
while True:
    input = pyperclip.paste()

    if len(input) < 100:
        # 开始检测
        if input != prevclip:
            print(u'新的剪贴板内容: ' + input)
            # 防重复检测
            prevclip = input

            if input.find('s/') != -1:  # Baiduyun: "链接：http://pan.baidu.com/s/1mhFoKxa 密码：w2le"
                # Search for extract code
                code = re.search('[\w\d]{6,10}', input).group(0)
                url = 'http://pan.baidu.com/s/' + code
                print(u'检测到百度云链接: ' + url)
                # Search for pwd
                input_trim = input[input.find(code) + 8:].lstrip()
                pwd = re.search('[\w\d]{4}', input_trim)
                if pwd is not None:
                    pwd = pwd.group(0)
                    prevclip = pwd
                    pyperclip.copy(pwd)
                    print(u'密码已复制到剪贴板: ' + pwd)
                webbrowser.open_new_tab(url)

            elif input.find('ab') != -1:  # acfun bangumi: ab1470255
                sear('ab\d+', 'http://acfun.tudou.com/v/', u'Acfun bangumi')

            elif input.find('ac') != -1:  # acfun video: ac2771372
                sear('ac\d+', 'http://www.acfun.tv/v/', u'Acfun video')

            elif input.find('av') != -1:  # bili video: av10000 av10001
                sear('av\d+', 'http://www.bilibili.com/video/', u'Bilibili video')

            elif input.find('sm') != -1:  # nico video: sm15853635
                sear('sm\d+', 'http://www.nicovideo.jp/watch/', u'Niconico video(sm)')

            elif input.find('so') != -1:  # nico video: so25829271
                sear('so\d+', 'http://www.nicovideo.jp/watch/', u'Niconico video(so)')

            elif input.find('lv') != -1:  # nico live: lv263651003
                sear('lv\d+', 'http://live.nicovideo.jp/watch/', u'Niconico live')

            elif input.find('id=') != -1:  # pixiv: id=57235066
                sear('id=\d+', 'http://www.pixiv.net/member_illust.php?mode=medium&illust_', u'Pixiv 作品 id')


    # 检测间隔
    time.sleep(0.6)
