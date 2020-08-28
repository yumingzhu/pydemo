# -*- coding: utf-8 -*
import datetime
import json
import os
import smtplib
import sys
import io
#设置python2 使用utf-8编码
# if sys.getdefaultencoding() != 'utf-8':
#     reload(sys)
#     sys.setdefaultencoding('utf-8')

# 获取用户信息
def loadFont(path):
    f = io.open(path, "r",encoding='utf-8')  # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    setting = json.load(f)
    f.close()
    return setting


# 发邮件
def senErrorEmail(ex, message):
    # 网易163邮箱
    HOST = 'smtp.163.com'
    # 2> 配置服务的端口，默认的邮件端口是25.
    PORT = '465'
    # 3> 指定发件人和收件人。
    FROM = '18612483486@163.com'
    # TO = '18612483486@163.com'
    receivers = ['zjw@gimc.cn','ymz@gimc.cn']

    # 4> 邮件标题
    SUBJECT = 'gimc-subentry-webapp执行出现错误了'
    # 5> 邮件内容
    CONTENT = message + "\n" + str(ex)

    # 创建邮件发送对象
    # 普通的邮件发送形式
    # smtp_obj = smtplib.SMTP()

    # 数据在传输过程中会被加密。
    smtp_obj = smtplib.SMTP_SSL(host=HOST)

    # 需要进行发件人的认证，授权。
    # smtp_obj就是一个第三方客户端对象
    smtp_obj.connect(host=HOST, port=PORT)

    # 如果使用第三方客户端登录，要求使用授权码，不能使用真实密码，防止密码泄露。
    res = smtp_obj.login(user=FROM, password='yu3486')
    print('登录结果：', res)

    # 发送邮件
    msg = '\n'.join(
        ['From: {}'.format(FROM), 'To: {}'.format(receivers), 'Subject: {}'.format(SUBJECT), '', CONTENT])  # ''此单引号不能少
    smtp_obj.sendmail(from_addr=FROM, to_addrs=receivers, msg=msg.encode('utf-8'))

print("开始执行了")
logDir = "/apps/logs/gimc-subentry-webapp/";
today = datetime.datetime.now().strftime('%Y-%m-%d')
logfile = logDir + "gimc-subentry-webapp-error-" + today + ".log";
settingPath = logDir + "Settings.json"

if (os.path.exists(logfile)):
    # 读取文件中的json数据
    setting = loadFont(settingPath)
    if (setting["date"] != today):
        setting["count"] = 0
        setting["date"] = today
        setting["fileSize"]=0
    fileInfo = os.stat(logfile)
    # 获取文件大小
    fileSize = fileInfo.st_size
    # 将当前文
    if(setting["fileSize"]<fileSize and setting["count"]<3):
        setting["fileSize"] = fileSize
        setting["count"] = setting["count"] + 1
        message = json.dumps(setting)
        print("发生邮箱------")
        senErrorEmail("", message)
        with open(settingPath, "w") as f:
            f.write(message)
