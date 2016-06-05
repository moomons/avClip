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
    input = pyperclip.paste().lstrip().rstrip()

    if len(input) < 100:
        # 开始检测
        if input != prevclip:
            print(u'新的剪贴板内容: ' + input)

            if input.find('av') != -1:         # Bilibili: av10000 av10001
                sear('av\d+', 'http://www.bilibili.com/video/', u'Bilibili video')

            elif input.find('s/') != -1:  # Baiduyun:
                # Search for extract code
                code = re.search('[\w\d]{8}', input).group(0)
                url = 'http://pan.baidu.com/s/' + code

                # Search for pwd
                input_trim = input[input.find(code) + 8:].lstrip()
                pwd = re.search('[\w\d]{4}', input_trim)
                if pwd is not None:
                    pwd = pwd.group(0)
                    pyperclip.copy(pwd)
                    print(u'检测到百度云链接, 密码已复制到剪贴板: ' + url + ' ' + pwd)
                else:
                    print(u'检测到百度云链接: ' + url)
                webbrowser.open_new_tab(url)

            elif input.find('lv') != -1:          # nico live: lv263651003
                no = re.search('lv[\d]+', input)
                if no is not None:
                    no = no.group(0)
                    url = 'http://live.nicovideo.jp/watch/' + no
                    print(u'检测到 niconico 直播: ' + url)
                    webbrowser.open_new_tab(url)

            elif input.find('id=') != -1:         # pixiv: id=57235066
                rematch = re.findall('id=\d+', input)
                for item in rematch:
                    url = 'http://www.pixiv.net/member_illust.php?mode=medium&illust_' + item
                    print(u'检测到 pixiv 作品 id: ' + url)
                    webbrowser.open_new_tab(url)

            # 防重复检测
            prevclip = input

    # 检测间隔
    time.sleep(0.6)
