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
    .add_xaxis(["cpu(%)", "memory", "网络(Mb)", "在线数量", "load 1min", "load 5min", "load 15min"])
    .add_yaxis("2.3.0", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("2.3.1", [66, 114, 87, 59, 195, 50, 69])
    .add_yaxis("2.2.1", [52, 104, 137, 129, 145, 60, 49])
    .add_yaxis("2.2.2", [50, 124, 147, 139, 135, 77, 59])
    .add_yaxis("2.2.3", [67, 134, 157, 159, 125, 64, 79])
    .add_yaxis("2.2.5", [77, 144, 167, 169, 165, 50, 39])
    .add_yaxis("2.2.6", [77, 144, 167, 169, 165, 50, 39])
    .add_yaxis("2.2.7", [77, 144, 167, 169, 165, 50, 39])
    .add_yaxis("2.2.8", [77, 144, 167, 169, 165, 50, 39])
    .add_yaxis("2.2.9", [77, 144, 167, 169, 165, 50, 39])
    .add_yaxis("2.2.10", [77, 144, 167, 169, 165, 50, 39])
    .add_yaxis("2.2.11", [77, 144, 167, 169, 165, 50, 39])
    .add_yaxis("2.2.12", [77, 144, 167, 169, 165, 50, 39])
    .set_global_opts(title_opts=opts.TitleOpts(title="压测性能统计"))
    # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
)
bar.render("perf.html")