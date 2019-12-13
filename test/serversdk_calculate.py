# -*- coding:utf-8 -*-
import re
import sys
from pyecharts.charts import Bar,Line
from pyecharts import options as opts


checklist = ['cpu_percent', 'percent', 'bps_rx', 'bps_tx', 'min1', 'min5', 'min15', 'online'] 
# file_path = '/Users/yueli/Desktop/health_check_case4_cpp_single_live_h265.txt' # TODO 自动匹配地址
file_path = sys.argv[1]

def calculat(check_op):
    with open(file_path, 'r') as f:
        data_list = []
        for line in f.readlines():
            # a = str(line)
            b = re.sub("[^a-zA-Z0-9\s.\w$]", '', str(line)) # 匹配数字、字母、英文{dot.}、下滑线
            list_b = b.strip().split(" ") # 把列表中的前后空格和换行符去掉
            if check_op in list_b:
                data = list_b.index(check_op) + 1
                data_list.append(list_b[data])
        del(data_list[-2:]) # 去除list最后两个数
        del(data_list[:2])  # 去除list前面两个数
        # print(data_list)
        return data_list

def avg(check_list):
    for check in checklist:
        sum_data = 0
        for item in calculat(check):
            sum_data += float(item)
        avg_data = '%.2f' % (sum_data / float(len(calculat(check)))) # 四舍五入取后两位

        if check == 'online':
            # online = avg_data
            online = (float(avg_data)/2)*8
            print('MediaServerSDK在线频道数是: %s' % online + '\n')
            # print((float(online)/2)*8)
        elif check == 'cpu_percent':
            cpu_percent = str(avg_data)
            print('服务器CPU使用率是: ' + cpu_percent + '%\n')
        elif check == 'percent':
            mem = str(avg_data)
            print('服务器Memory使用率是: ' + mem + '%\n')
        elif check == 'bps_rx': 
            net_rx = '%.2f' % (float(avg_data) / 1000000 / 8) # 带宽换算，从 bps 换算到 MB/s
            print('服务器网络rx: ' + str(net_rx) + ' MB/s\n') 
        elif check == 'bps_tx': 
            net_tx = '%.2f' % (float(avg_data) / 1000000 / 8) # 带宽换算，从 bps 换算到 MB/s
            print('服务器网络tx: ' + str(net_tx) + ' MB/s\n')    
        else:
            load = str(avg_data)
            print('服务器load average ' + check + ' 是: ' + load + '\n')
            if check == 'min1':
                min1 = str(avg_data)
            elif check == 'min5':
                min5 = str(avg_data)
            else:
                min15 = str(avg_data)
    # return cpu_percent, mem, net_rx, net_tx, min1, min5, min15, online
    return cpu_percent, mem, net_rx, net_tx, min1, min5, min15

# if __name__ == "__main__":
#     avg(checklist)
    # calculat(check_op='cpu_percent')
    # calculat(check_op='cpu_percent')

import logging
import logging.config


logging.basicConfig(
    format='%(name)s:%(lineno)d - %(levelname)s - %(message)s',
    level=logging.DEBUG)


# 柱状图
bar = Bar()
bar.add_xaxis(["CPU(%)", "Memory(Gb)", "net_rx(MB/s)", "net_tx(MB/s)", "min1", "min5", "min15"])
bar.add_yaxis("serversdk二期上官网版本", avg(checklist))
bar.set_global_opts(title_opts={"text": "性能统计", "subtext": "\n", "subtext": "recording sdk"})
bar.set_global_opts(title_opts=opts.TitleOpts(title="test for performance"))
# bar.set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-10)))
bar.set_global_opts(yaxis_opts=opts.AxisOpts())
bar.render()



# def avg(check_list):
#     for check in checklist:
#         sum_data = 0
#         for item in calculat(check):
#             sum_data += float(item)
#         avg_data = '%.2f' % (sum_data / float(len(calculat(check)))) # 四舍五入取后两位
#         if check == 'online':
#             cnt = avg_data
#             # print('Recording AgoraCoreService online is: ' + str(avg_data) + '\n')
#         elif check == 'cpu_percent':
#             cpu = avg_data
#             # print('performance machine\'s CPU use percent is: ' + str(avg_data) + '%\n')
#         elif check == 'percent':
#             mem = avg_data
#             # print('performance machine\'s MEM use percent is: ' + str(avg_data) + '%\n')
#         elif check == 'bps_rx': 
#             net = '%.2f' % (float(avg_data) / 1000000 / 8) # 带宽换算，从 bps 换算到 MB/s
#             # print('performance machine\'s NETWORK use is: ' + str(net) + ' MB/s\n')   
#         else:
#             print('performance machine\'s system load average ' + check + ' is: ' + str(avg_data) + '\n')
#     return cnt, cpu, mem, net


# bar = ()
#     Bar()
#     .add_xaxis(
#         [
#         "CPU(%)", 
#         "Mem(Gb)", 
#         "网络(rx:MB/S)",
#         "在线数(个)", 
#         "load 1min", 
#         "load 5min", 
#         "load 15min"
#         ]
#     )
#     .add_yaxis("直播-单流", [cpu, mem, net, cnt, 19.9, 21.43, 22.76])
#     # .add_yaxis("直播-合图", [47.6, 3.2, 2.83, 50, 7.33, 7.83, 8.03])
#     # .add_yaxis("直播-裸数据", [40.4, 3.58, 6.79, 120, 10.62, 8.82, 8.9])
#     .set_global_opts(
#         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-10)),
#         yaxis_opts=opts.AxisOpts()
#     )
# )
# bar.render("perf.html")




# def avg(file_path, check_list):
#     with open(file_path, 'r') as f:
#         data_list = []
#         check_data = check_list
#
#         for line in f.readlines():
#             list_a = line.strip().split(",")
#             list_b = [x.strip() for x in list_a]
#
#             if check_data in list_b:
#                 data = list_b.index(check_data) + 1
#                 # print(data)
#                 data_list.append(list_b[data])
#         sum_data = 0
#         for item in data_list:
#             sum_data += float(item)
#         # print(sum)
#         avg_data = sum_data / float(len(data_list))
#         print('performance machine\'s ' + check_data + ' is:\n' + str(avg_data))

# avg(file_path, checklist)
# print(type(checklist))

# 获取平均数
# def Get_Average(list):
#     sum = 0
#     for item in list:
#         sum += float(item)
#     return sum / float(len(list))
#
#
# # 最大数
# def Get_Max(list):
#     return max(list)
#
#
# # 最小数
# def Get_Min(list):
#     return min(list)
#
#
# # 极差
# def Get_Range(list):
#     return max(list) - min(list)
#
#
# # 中位数
# def get_median(data):
#     data = sorted(data)
#     size = len(data)
#     if size % 2 == 0:
#         # 判断列表长度为偶数
#         median = (data[size // 2] + data[size // 2 - 1]) / 2
#     if size % 2 == 1:
#         # 判断列表长度为奇数
#         median = data[(size - 1) // 2]
#     return median
#
#
# # 众数(返回多个众数的平均值)
# def Get_Most(list):
#     most = []
#     item_num = dict((item, list.count(item))
#                     for item in list)
#     for k, v in item_num.items():
#         if v == max(item_num.values()):
#             most.append(k)
#     return sum(most) / len(most)

# for line in f:
# result.append(list(line.strip('cpu_percent').split(',')[0]))

# import numpy as np
# f = open('/Users/yueli/Desktop/linux_share/test/health_check_case1_cpp_single_live_240p.txt')
# line = f.readline()
# data_list = []
# while line:
#     num = list(map(str,line.split('cpu_percent')))
#     data_list.append(num)
#     line = f.readline()
# f.close()
# data_array = np.array(data_list)
# print(data_array)
