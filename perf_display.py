#! coding=utf-8
from pyecharts.charts import Bar
from pyecharts import options as opts
import sys
# result = []
# with open('/Users/yueli/Desktop/linux_share/test/health_check_case1_cpp_single_live_240p.txt', 'r') as f:
#     for line in f:
#         # result.append(list(line.strip('cpu_percent').split(',')[0]))
#         result = f.readlines()
# print(result)

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


# 生成表格
bar = (
    Bar()
    .add_xaxis(["CPU(%)", "Mem(Gb)", "网络(rx:MB/S)", "在线数(个)", "load 1min", "load 5min", "load 15min"])
    .add_yaxis("2.3.3.150_1080p_1", [70.66, 9.88, 175.76, 500, 23.37, 20.51, 20.58])
    .add_yaxis("2.3.3.150_1080p_2", [60, 9.3, 0, 450, 0, 0, 16])
    .add_yaxis("2.3.3.150_240p_1", [78.50, 9.83, 26.18, 700, 25.63, 26.82, 25.39])
    .add_yaxis("2.3.3.150_240p_2", [60, 8.6, 0, 550, 0, 0, 16])
    # .add_xaxis("2.3.3")
    # .add_yaxis("2.2.1", [52, 104, 137, 129, 145, 60, 49])
    # .add_yaxis("2.2.2", [50, 124, 147, 139, 135, 77, 59])
    # .add_yaxis("2.2.3", [67, 134, 157, 159, 125, 64, 79])
    # .add_yaxis("2.2.5", [77, 144, 167, 169, 165, 50, 39])
    # .add_yaxis("2.2.6", [77, 144, 167, 169, 165, 50, 39])
    # .add_yaxis("2.2.7", [77, 144, 167, 169, 165, 50, 39])
    # .add_yaxis("2.2.8", [77, 144, 167, 169, 165, 50, 39])
    # .add_yaxis("2.2.9", [77, 144, 167, 169, 165, 50, 39])
    # .add_yaxis("2.2.10", [77, 144, 167, 169, 165, 50, 39])
    # .add_yaxis("2.2.11", [77, 144, 167, 169, 165, 50, 39])
    # .add_yaxis("2.2.12", [77, 144, 167, 169, 165, 50, 39])
    .set_global_opts(title_opts=opts.TitleOpts(title="压测性能统计"))
    # .set_global_opts(title_opts={"text": "性能统计", "subtext": "server_sdk"})
)
bar.render("server_sdk_perf.html")