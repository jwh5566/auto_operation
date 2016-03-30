#!/usr/bin/env python
# coding=utf-8
__author__ = 'root'

import httplib

import dns.resolver

iplist = []
appdomain = 'www.qq.com'


def get_iplist(domain=''):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception, e:
        print 'dns resolver error: ' + str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j)  # dns object--> list
    return True


def checkip(ip):
    checkurl = ip + ':80'
    getcontent = ''
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)
    try:
        conn.request('GET', '/', headers={"Host": appdomain})
        r = conn.getresponse()
        getcontent = r.read(15)
    finally:
        if getcontent == '<！doctype html>':
            print ip + " [OK]"
        else:
            ip + " [Error]"


if __name__ == '__main__':
    if get_iplist(appdomain) and len(iplist) > 0:
        print iplist
        for ip in iplist:
            print ip
            checkip(ip)
    else:
        print "dns resolver error."
