#!/usr/bin/env python
# coding=utf-8
__author__ = 'root'
import rrdtool
import time

import psutil

total_input_traffic = psutil.net_io_counters()[1]
total_output_traffic = psutil.net_io_counters()[0]
starttime = int(time.time())
# 将获取到的三个数据作为updatev的参数，返回{'return_value'： 0L}则说明更新成功，反之失
# 败
print total_input_traffic
print total_output_traffic
update = rrdtool.updatev('/var/tmp/Flow.rrd',
                         '%s:%s:%s' % (str(starttime), str(total_input_traffic), str(total_output_traffic)))
print update
