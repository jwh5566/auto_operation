#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/31'

import xlsxwriter
from chapter2  import img
workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook.add_worksheet()  # 创建一个工作表对象
# worksheet.set_column('A: A', 20)  # 设定第一列（A）宽度为20像素  有问题
bold = workbook.add_format({'bold': True})  #  定义一个加粗的格式对象
worksheet.write('A1', 'Hello')
worksheet.write('A2', 'World', bold)
worksheet.write('B2', u'中文测试', bold)
worksheet.write(2, 0, 32)
worksheet.write(3, 0, 35.5)  # 行列表示法 3行0列
worksheet.write(4, 0, '=SUM(A3:A4)')    # 第五行

worksheet.insert_image('B5', 'img/2.jpg')
workbook.close()
