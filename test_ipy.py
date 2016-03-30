#!/usr/bin/env python
# coding=utf-8
__author__ = 'root'

from IPy import IP
# print  IPy.IP('10.0.0.1').version()

ip = IP('192.168.0.0/16')
print ip.len()
# for x in ip:
#     print x
print ip.iptype()
