import smtplib
from email.mime.text import MIMEText


def encode_html(s):
    rtn = str(s)
    rtn = rtn.replace("<", "&lt")
    rtn = rtn.replace(">", "&gt")
    return rtn


def send_mail(title="title", content='content'):
    print("send_mail()")

    content = encode_html(content)

    # 设置服务器所需信息
    # QQ邮箱服务器地址
    mail_host = 'smtp.qq.com'
    port = 465
    # QQ邮箱用户名
    mail_user = '12345678@qq.com'
    # 密码(部分邮箱为授权码)
    mail_pass = '12345678'

    # 邮件发送方邮箱地址
    sender = mail_user
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = [mail_user]

    # 设置email信息
    # 邮件内容设置
    message = MIMEText(content, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = title
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        # 连接到服务器
        smtpObj.connect(mail_host, port)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误

    return True


if __name__ == "__main__":
    send_mail("title", 'content')
