#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    使用网易163向qq邮箱发送测试邮件
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/31'

import smtplib
import string
HOST = 'smtp.163.com'
SUBJECT = 'Test mail from python'
TO = '419288922@qq.com'
FROM = 'jwh5566@163.com'
text = 'Python rules them all!'
BODY = string.join(
    ("From: %s" % FROM,
    "To: %s" %TO,
    "Subject: %s" %SUBJECT,
    "",
    text), '\r\n'
)
server = smtplib.SMTP()
server.connect(HOST, '25')
# server.starttls()  使用gmail的时候需要
server.login('jwh5566@163.com', 'XXXXXXX')
server.sendmail(FROM, [TO], BODY)
server.quit()

