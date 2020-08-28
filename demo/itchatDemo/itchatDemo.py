import time
from timeit import Timer

import requests
import itchat


# 发送消息
def sendNews():
    # global my_love
    try:
        itchat.login()  # 只是普通的登陆，并不具有缓存的功能
        itchat.auto_login(hotReload=True)  # 可以暂存登陆状态
        friend = itchat.search_friends(u'mwz')[0]  # XX为好友的备注或名称
        text = "我是老孟同志"
        while True:
            itchat.send_msg(text, friend["UserName"])  # text是要发送的内容
            time.sleep(120)
        # 给微信好友发送消息

    except:
        msg4 = "出错了  ！！！"


# itchat.logout()


# 调试函数
def test():
    itchat.auto_login()
    itchat.send(u'测试消息发送', 'filehelper')  # 发送给文件助手


if __name__ == '__main__':
    sendNews()
