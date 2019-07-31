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
        # "CPU core",
        "CPU(%)", 
        "Mem(Gb)", 
        "网络(rx:MB/S)",
        "在线数(个)", 
        "load 1min", 
        "load 5min", 
        "load 15min"
        ]
    )
    .add_yaxis("通信-单流", [72.34, 5.08, 7.25, 175, 17.62, 17.4, 17.09])
    .add_yaxis("通信-合图", [50.39, 3.17, 2.01, 50, 8.64, 9.25, 9.11])
    .add_yaxis("通信-裸数据", [49.78, 4.14, 5.08, 120, 9.43, 9.32, 9.13])
    .add_yaxis("直播-单流", [])
    .add_yaxis("直播-合图", [])
    .add_yaxis("直播-裸数据", [])
    .add_yaxis("unify-单流", [])
    .add_yaxis("unify-合图", [])
    .add_yaxis("unify-裸数据", [])

    # .set_global_opts(title_opts=opts.TitleOpts(title="压测性能统计"))
    # .set_global_opts(title_opts=opts.TitleOpts(title="\n"))
    # .set_global_opts(title_opts={"text": "性能统计", "subtext": "\n"})
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-10)),
        yaxis_opts=opts.AxisOpts()
        # title_opts={"text": "性能统计", "subtext": "\n", "subtext": "recording sdk"},
        # title_opts=opts.TitleOpts(title="压测性能统计")
    )
)
bar.render("recording_sdk_perf.html")