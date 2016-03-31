#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    实现带附件格式的业务服务质量周报邮件
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/31'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = 'smtp.163.com'
SUBJECT = u'官网业务服务质量周报'
TO = '419288922@qq.com'
FROM  = 'jwh5566@163.com'
def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage
msg = MIMEMultipart('related')
msgtext = MIMEText('<font color=red>官网业务平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>', 'html', 'utf-8')
msg.attach(msgtext)
msg.attach(addimg('img/1.jpg', 'weekly'))
attach = MIMEText(open('doc/week_report.xlsx', 'rb').read(), 'base64', 'utf-8')
attach['Content-Type'] = 'application/octet-stream'
attach['Content-Disposition'] = 'attachment; filename=\"业务服务质量周报(12周).xlsx\"'.decode('utf-8').encode('gb18030')
msg.attach(attach)
msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
try:
    server = smtplib.SMTP()
    server.connect(HOST, '25')
    # server.starttls()
    server.login('jwh5566@163.com', 'XXXXXXXX')
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print '邮件发送成功！'
except Exception, e:
    print '失败：' + str(e)


