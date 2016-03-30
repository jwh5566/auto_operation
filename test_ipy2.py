#!/usr/bin/env python
# coding=utf-8
__author__ = 'root'

from IPy import IP

ip_s = raw_input('please input a ip or net range: ')
ips = IP(ip_s)
if len(ips) > 1:  # net address
    print 'net: %s' % ips.net()
    print 'netmask: %s' % ips.netmask()
    print 'broadcast: %s' % ips.broadcast()
    print 'reverse address: %s' % ips.reverseName()
    print 'subnet: %s' % len(ips)
else:  # single ip address
    print 'reverse address: %s' % ips.reverseName()
    print 'hexadecimal: %s' % ips.strHex()
    print 'binary ip: %s' % ips.strBin()
    print 'iptype: %s' % ips.iptype()
