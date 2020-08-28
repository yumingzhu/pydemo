import smtplib


def senErrorEmail(ex, message):
    # 网易163邮箱
    HOST = 'smtp.163.com'
    # 2> 配置服务的端口，默认的邮件端口是25.
    PORT = '465'
    # 3> 指定发件人和收件人。
    FROM = '18612483486@163.com'
    # TO = '18612483486@163.com,648500318@qq.com'
    receivers = ['ymz@gimc.cn',"18612483486@163.com"]
    # 4> 邮件标题
    SUBJECT = 'gimc-subentry-webapp执行出现错误了'
    # 5> 邮件内容
    CONTENT = message + "\n" + str(ex)

    # 创建邮件发送对象
    # 普通的邮件发送形式
    #smtp_obj = smtplib.SMTP()

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



if __name__ == '__main__':
    senErrorEmail("1111", "1111111")