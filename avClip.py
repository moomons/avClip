# -*- coding: utf-8 -*-
#!/usr/bin/env python
import webbrowser
import pyperclip
import time
import re

"""
测试用:
【Bilibili】
input = u"av10000"

【百度云】
input = u"链接：http://pan.baidu.com/s/1mhFoKxa 密码：w2le"

【360云盘】

"""

# input = u"链接：http://pan.baidu.com/s/1mhFoKxa 密码：w2le"
#
# # Search for extract code
# code = re.search("[\w\d]{8}", input).group(0)
# url = "http://pan.baidu.com/s/" + code
#
# # Search for pwd
# input_trim = input[input.find(code)+8:].lstrip()
# pwd = re.search("[\w\d]{4}", input_trim)
# if pwd is not None:
#     pwd = pwd.group(0)
#     pyperclip.copy(pwd)
#     print(u'检测到百度云链接, 密码已复制到剪贴板: ' + url + " " + pwd)
# else:
#     print(u'检测到百度云链接: ' + url)
#
# exit(0)

prevclip = ""
while True:
    input = pyperclip.paste().lstrip().rstrip()

    # 开始检测
    if input != prevclip:
        print(u'新的剪贴板内容: ' + input)

        if input.startswith('av'):  # Bilibili
            avnumber = input[2:].rstrip()
            try:
                number = int(avnumber)
                url = "http://www.bilibili.com/video/av" + avnumber + "/"
                print(u'检测到 Bilibili av号: ' + url)
                webbrowser.open_new_tab(url)
            except ValueError:
                print(u'检测到无效av号.')

        elif input.find("pan.baidu") != -1:  # Baiduyun:
            # Search for extract code
            code = re.search("[\w\d]{8}", input).group(0)
            url = "http://pan.baidu.com/s/" + code

            # Search for pwd
            input_trim = input[input.find(code) + 8:].lstrip()
            pwd = re.search("[\w\d]{4}", input_trim)
            if pwd is not None:
                pwd = pwd.group(0)
                pyperclip.copy(pwd)
                print(u'检测到百度云链接, 密码已复制到剪贴板: ' + url + " " + pwd)
            else:
                print(u'检测到百度云链接: ' + url)
            webbrowser.open_new_tab(url)

        elif input.find("lv") != -1:          # nico live: lv263651003
            no = re.search("lv[\d]+", input)
            if no is not None:
                no = no.group(0)
                url = "http://live.nicovideo.jp/watch/" + no
                print(u'检测到 niconico 直播: ' + url)
                webbrowser.open_new_tab(url)

        elif input.find("id=") != -1:         # pixiv: id=57235066
            parse = input[input.find("id="):].lstrip()
            no = re.search("[\d]+", parse)
            if no is not None:
                no = no.group(0)
                url = "http://www.pixiv.net/member_illust.php?mode=medium&illust_id=" + no
                print(u'检测到 pixiv 作品 id: ' + url)
                webbrowser.open_new_tab(url)

        # 防重复检测
        prevclip = input

    # 检测间隔
    time.sleep(0.6)
