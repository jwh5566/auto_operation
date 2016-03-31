#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/31'
import os, sys
import time
import pycurl

URL = 'www.baidu.com'
c = pycurl.Curl()
c.setopt(pycurl.URL, URL)
c.setopt(pycurl.CONNECTTIMEOUT, 5)  # 定义请求连接的等待时间
c.setopt(pycurl.TIMEOUT, 5)
c.setopt(pycurl.NOPROGRESS, 1)   # 不屏蔽下载进度条
c.setopt(pycurl.FORBID_REUSE, 1)  # 完成交换后 强制断开连接
c.setopt(pycurl.MAXREDIRS, 1)    # 指定HTTP重定向的最大数为1
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)  # 设置保存DNS信息的时间为30秒
indexfile = open(os.path.dirname(os.path.realpath(__file__))+'/content.txt', 'wb')
c.setopt(pycurl.WRITEHEADER, indexfile)  #  将返回的头部信息重定向到indexfile文件
c.setopt(pycurl.WRITEDATA, indexfile)  # 将返回的html数据重定向到indexfile文件

try:
    c.perform()
except Exception, e:
    print 'Connection Error: '+ str(e)
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE =  c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)

print "HTTP状态码：%s" %(HTTP_CODE)
print "DNS解析时间：%.2f ms"%(NAMELOOKUP_TIME*1000)
print "建立连接时间：%.2f ms" %(CONNECT_TIME*1000)
print "准备传输时间：%.2f ms" %(PRETRANSFER_TIME*1000)
print "传输开始时间：%.2f ms" %(STARTTRANSFER_TIME*1000)
print "传输结束总时间：%.2f ms" %(TOTAL_TIME*1000)
print "下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD)
print "HTTP头部大小：%d byte" %(HEADER_SIZE)
print "平均下载速度：%d bytes/s" %(SPEED_DOWNLOAD)
#关闭文件及Curl对象
indexfile.close()
c.close()