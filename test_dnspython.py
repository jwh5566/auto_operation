#!/usr/bin/env python
# coding=utf-8
__author__ = 'root'
import dns.resolver

domain = raw_input('Please input an domain： ')
A = dns.resolver.query(domain, 'A')
# print A.response.answer
for i in A.response.answer:
    # print i
    for j in i.items:
        print j
