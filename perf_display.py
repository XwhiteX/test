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
    .add_xaxis(
        [
        "CPU core", 
        "CPU(%)", 
        "Mem(Gb)", 
        "网络(tx:MB/S)", 
        "在线数(个)", 
        "load 1min", 
        "load 5min", 
        "load 15min"
        ]
    )
    .add_yaxis("2.3.3.150_1080p_1", [16, 70.66, 9.88, 175.76, 500, 23.37, 20.51, 20.58])
    .add_yaxis("2.3.3.150_1080p_2", [16, 60, 9.3, 0, 450, 0, 0, 16])
    .add_yaxis("2.3.3.150_240p_1", [16, 78.50, 9.83, 26.18, 700, 25.63, 26.82, 25.39])
    .add_yaxis("2.3.3.150_240p_2", [16, 60, 8.6, 0, 550, 0, 0, 16])
    .add_yaxis("1期plus_2.3.3.150_240p", [8, 56.89, 6.4, 13.08, 380, 5.08, 5.078, 5.205])

    # .set_global_opts(title_opts=opts.TitleOpts(title="压测性能统计"))
    # .set_global_opts(title_opts=opts.TitleOpts(title="\n"))
    # .set_global_opts(title_opts={"text": "性能统计", "subtext": "\n"})
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-10)),
        title_opts={"text": "性能统计", "subtext": "\n", "subtext":"media server sdk"},
    )
)
bar.render("server_sdk_perf.html")