#! /usr/bin/env python
# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from configparser import ConfigParser
from smtplib import SMTP_SSL

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 配置文件初始化
config = ConfigParser()
# 配置文件的绝对路径
config_path = os.path.dirname(os.path.realpath(__file__)) + "/config.ini"
# 读取配置文件
config.read(filenames=config_path, encoding='UTF-8')

# 邮箱smtp服务器
host_server = config.get(section="Mail", option="host_server")
print(host_server)
# sender_mail为发件人的邮箱
sender_mail = config.get(section="Mail", option="sender_mail")
# pwd为邮箱的授权码
pwd = config.get(section="Mail", option="pwd")  ##
# 发件人的邮箱
sender_fj_mail = config.get(section="Mail", option="sender_fj_mail")
# 收件人邮箱
receivers = config.get(section="Mail", option="receivers").split(',')

# 邮件的正文内容
mail_content = config.get(section="Mail", option="mail_content")
# 邮件标题
mail_title = config.get(section="Mail", option="mail_title")

# 邮件正文内容
msg = MIMEMultipart()
# msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_fj_mail
# msg["To"] = Header("接收者的别名", 'utf-8')  ## 接收者的别名

for to_mail_name in receivers:
    msg.add_header("to", to_mail_name)

# 邮件正文内容
msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

# 附件路径
FilePath = config.get(section="Mail", option="FilePath").split(',')  # ['Mail.py','MailMain.py']
for filename in FilePath:
    filefj = MIMEText(open(str(filename), 'rb').read(), 'base64', 'utf-8')
    filefj.add_header('Content-Type', 'application/octet-stream')
    filefj.add_header('Content-Disposition', 'attachment; filename="' + filename + '"')
    msg.attach(filefj)

server = smtplib.SMTP_SSL(host_server, 465)
server.set_debuglevel(1)
server.connect(host_server, 465)
server.ehlo()  # 若不加这行,在服务器环境会报错SMTPServerDisconnected("Connection unexpectedly closed")
server.login(sender_mail, pwd)
server.sendmail(sender_fj_mail, receivers, msg.as_string())
server.quit()
