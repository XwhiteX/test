# coding=utf-8
# from urllib import request
# from http import cookiejar
#
# if __name__ == '__main__':
#     # 声明一个CookieJar对象实例来保存cookie
#     cookie = cookiejar.CookieJar()
#     # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
#     handler=request.HTTPCookieProcessor(cookie)
#     # 通过CookieHandler创建opener
#     opener = request.build_opener(handler)
#     # 此处的open方法打开网页
#     response = opener.open('http://www.baidu.com')
#     # 打印cookie信息
#     for item in cookie:
#         print('Name = %s' % item.name)
#         print('Value = %s' % item.value)

import requests
import json
import os
import sys

def download_with_auth(self):
    """Prepare the auth info if needed"""
    # auth_opt = "--http-user %s --http-passwd %s" % (self.user, self.pw) if self.user != "" and self.pw != "" else ""
    # get_cmd = "cd %s;wget -c -T 600 %s %s" % (self.home_build_dir, auth_opt, self.url)

    head = {"Content-Type": "application/x-www-form-urlencoded"}
    auth_url = "https://oauth.agoralab.co/oauth/token"
    data = {"grant_type": "password", "client_id": "U2eggysiyiXjMmKUHt57H3Zq5bgR0iP0",
            "client_secret": "JC1P5xrJ0aYqZeNLik6luABfD0D6CMAohwPWME6qIyfq1sYaGLBnEfd6Mbw8xElm",
            "username": "pvYAy8Sv", "password": "5uh8glqSvy1I2m1N"}

    res = requests.post(auth_url, data=data, headers=head)
    a = res.content.decode('utf-8')
    token = json.loads(a)["access_token"]
    cookie = "Cookie:accessToken=%s" % token

    # cookie = "Cookie:accessToken=2993d00bc58ba3382a37f4d42d0d73efb6bfa088"
    # self.download_cmd = "cd %s && curl -H %s -O %s " % (self.home_build_dir, cookie, self.url)
    download_cmd = "curl -H %s -O %s" % (cookie, self)
    # LinuxCmd(download).run_cmd(timeout=600)
    os.system(download_cmd)

url = sys.argv[1]
d = download_with_auth(url)
# b = download_with_auth('https://release.agoralab.co/disk/v2.3.3.150_sei/AgoraSDK/Linux/testing/Agora_Server_SDK_for_Linux_v2_3_3_150_sei_FULL_20190427_1066.tar.gz')