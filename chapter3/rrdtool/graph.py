#!/usr/bin/env python
# coding=utf-8
__author__ = 'root'
import rrdtool
import time

title = 'Server network traffic flow (' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ')'
# 重点解释"--x-grid"，"MINUTE：12：HOUR：1：HOUR：1：0：%H"参数的作用（从左往右进行分
# 解）
# “MINUTE：12”表示控制每隔12分钟放置一根次要格线
# “HOUR：1”表示控制每隔1小时放置一根主要格线
# “HOUR：1”表示控制1个小时输出一个label标签
# “0：%H”0表示数字对齐格线，%H表示标签以小时显示
# rrdtool.graph("Flow.png", "--start", "-1d", "--vertical-label=Bytes/s",
#               "--x-grid", "MINUTE: 12: HOUR: 1: HOUR: 1: 0: %H",
#               "--width", "650","--height","230","--title", title,
#               "DEF：inoctets=Flow.rrd：eth0_in：AVERAGE", #指定网卡入流量数据源DS及CF
#             "DEF：outoctets=Flow.rrd：eth0_out：AVERAGE", #指定网卡出流量数据源DS及CF
#             "CDEF：total=inoctets，outoctets，+", #通过CDEF合并网卡出入流量，得出总流量
#             # total
#             "LINE1：total#FF8833：Total traffic", #以线条方式绘制总流量
#             "AREA：inoctets#00FF00：In traffic", #以面积方式绘制入流量
#             "LINE1：outoctets#0000FF：Out traffic", #以线条方式绘制出流量
#             "HRULE：6144#FF0000：Alarm value\\r", #绘制水平线，作为告警线，阈值为6.1k
#             "CDEF：inbits=inoctets，8，*", #将入流量换算成bit，即*8，计算结果给inbits
#             "CDEF：outbits=outoctets，8，*", #将出流量换算成bit，即*8，计算结果给outbits
#             "COMMENT：\\r", #在网格下方输出一个换行符
#             "COMMENT：\\r",
#             "GPRINT：inbits：AVERAGE：Avg In traffic\： %6.2lf %Sbps", #绘制入流量平均
#             # 值
#             "COMMENT： ",
#             "GPRINT：inbits：MAX：Max In traffic\： %6.2lf %Sbps",#绘制入流量最大值
#             "COMMENT： ",
#             "GPRINT：inbits：MIN：MIN In traffic\： %6.2lf %Sbps\\r", #绘制入流量最小值
#             "COMMENT： ",
#             "GPRINT：outbits：AVERAGE：Avg Out traffic\： %6.2lf %Sbps", #绘制出流量平
#             # 均值
#             "COMMENT： ",
#             "GPRINT：outbits：MAX：Max Out traffic\： %6.2lf %Sbps", #绘制出流量最大值
#             "COMMENT： ",
#             "GPRINT：outbits：MIN：MIN Out traffic\： %6.2lf %Sbps\\r"
#               )
#             #绘制出流量最
#             # 小值

rrdtool.graph("Flow.png", "--start", "-1d", "--vertical-label=Bytes/s", "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H", \
              "--width", "650", "--height", "230", "--title", title,
              "DEF:inoctets=/var/tmp/Flow.rrd:eth0_in:AVERAGE",
              "DEF:outoctets=/var/tmp/Flow.rrd:eth0_out:AVERAGE",
              "CDEF:total=inoctets,outoctets,+",
              "LINE1:total#FF8833:Total traffic",
              "AREA:inoctets#00FF00:In traffic",
              "LINE1:outoctets#0000FF:Out traffic",
              "HRULE:6144#FF0000:Alarm value\\r",
              "CDEF:inbits=inoctets,8,*",
              "CDEF:outbits=outoctets,8,*",
              "COMMENT:\\r",
              "COMMENT:\\r",
              "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
              "COMMENT:   ",
              "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps",
              "COMMENT:  ",
              "GPRINT:inbits:MIN:MIN In traffic\: %6.2lf %Sbps\\r",
              "COMMENT: ",
              "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
              "COMMENT: ",
              "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps",
              "COMMENT: ",
              "GPRINT:outbits:MIN:MIN Out traffic\: %6.2lf %Sbps\\r")
