# encoding: utf-8
# Author    : damionfan@163.com
# Datetime  : 2020/2/16 15:09
# User      : Damion Fan
# Product   : PyCharm
# Project   : arxiv
# File      : email2user.py
# explain   : 文件说明
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "damionfan"  # 用户名
mail_pass = "fsy19970828"  # 授权密码，非登录密码

sender = 'damionfan@163.com'  # 发件人邮箱(最好写全, 不然会失败)


def sendEmail(receivers, title, content):
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()


def Satrt_email(title, content):
    target_list = ['20737506@qq.com', 'damionfan@163.com']
    # title = 'Today paper!'
    # content = 'arxiv 测试'
    sendEmail(target_list, title, content)
