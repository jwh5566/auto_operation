#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    定制自动化业务流量报表周报
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/31'
import xlsxwriter
workbook = xlsxwriter.Workbook('chart.xlsx')
worksheet = workbook.add_worksheet()
chart = workbook.add_chart({'type': 'column'})  # 柱状图
title = [u'业务名称', u'星期一', u'星期二', u'星期三', u'星期四', u'星期五', u'星期六', u'星期日', u'平均流量']
buname = [u'业务官网', u'新闻中心', u'购物频道', u'体育频道', u'亲子频道']  #定义频道名称
# 定义五个频道一周的流量表
data = [
    [150, 152, 158, 149, 155, 145, 148],
    [89, 88, 95, 93, 98, 100, 99],
    [201, 200, 198, 175, 170, 198, 195],
    [75, 77, 78, 78, 74, 70, 79],
    [88, 85, 87, 90, 93, 88, 84],
]
format = workbook.add_format()
format.set_border(1)
format_title = workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#cccccc')
format_title.set_align('center')
format_title.set_bold()

format_ave = workbook.add_format()
format_ave.set_border(1)
format_ave.set_num_format('0.00')
# 写入excel
worksheet.write_row('A1', title, format_title)
worksheet.write_column('A2', buname, format)
worksheet.write_row('B2', data[0], format)
worksheet.write_row('B3', data[1], format)
worksheet.write_row('B4', data[2], format)
worksheet.write_row('B5', data[3], format)
worksheet.write_row('B6', data[4], format)

def chart_series(cur_row):  # cur_row 代表2 - 6行的数据
    # 写入公式类数据
    worksheet.write_formula('I'+cur_row, '=AVERAGE(B'+cur_row+':H'+cur_row+')', format_ave)
    chart.add_series({
        'categories': '=Sheet1!$B1:$H1',
        'values'    : '=Sheet1!$B$'+cur_row+':$H'+cur_row,
        'line'      : {'color': 'black'},
        'name'      : '=Sheet1!$A$'+cur_row,
    })
for row in range(2, 7):
    chart_series(str(row))
chart.set_size({'width': 577, 'height': 287})
chart.set_title({'name': u'业务流量周报图表'})  # 图标上方的标题
chart.set_y_axis({'name': 'Mb/s'})  # 设置y轴标题
worksheet.insert_chart('A8', chart)
workbook.close()

