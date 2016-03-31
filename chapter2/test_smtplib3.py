#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    实现图文格式的服务器性能报表邮件
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/31'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = 'smtp.163.com'
SUBJECT = u'业务性能数据报表'
TO = '419288922@qq.com'
FROM = 'jwh5566@163.com'
def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage
msg = MIMEMultipart('related')   # related 定义内嵌的邮件体，而不是作为附件
msgtext = MIMEText("""
<table width="600" border="0" cellspacing="0" cellpadding="4">
      <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
        <td colspan=2>*官网性能数据  <a href="monitor.domain.com">更多>></a></td>
      </tr>
      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
        <td>
         <img src="cid:io"></td><td>
         <img src="cid:key_hit"></td>
      </tr>
      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
         <td>
         <img src="cid:men"></td><td>
         <img src="cid:swap"></td>
      </tr>
    </table>""","html","utf-8")
msg.attach(msgtext)
msg.attach(addimg('img/1.jpg', 'io'))
msg.attach(addimg('img/2.jpg', 'key_hit'))
msg.attach(addimg('img/3.jpg', 'men'))
msg.attach(addimg('img/4.jpg', 'swap'))
msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
try:
    server = smtplib.SMTP()
    server.connect(HOST, '25')
    # server.starttls()
    server.login('jwh5566@163.com', 'jwh19880313')
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print '邮件发送成功！'
except Exception, e:
    print '失败：' + str(e)

