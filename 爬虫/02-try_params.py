# coding=utf-8
import requests


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
# p = {"wd":"传智播客"}
# # url_temp = "http://www.baidu.com/s?" 带不带问号都行
# url_temp = "http://www.baidu.com/s"


# r = requests.get(url_temp, headers=headers, params=p)
# print(r.status_code)
# print(r.request.url)

url = "http://www.baidu.com/s?wd={}".format("传智播客")
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.request.url)
