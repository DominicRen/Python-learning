# coding=utf-8
import requests


# 发送请求
response = requests.get("https://www.baidu.com/img/xinshouye_d63d8cd784cea6223a26e3ce33344353.png")
# 保存
with open("a.png", "wb") as f:
    f.write(response.content)
