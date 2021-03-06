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
    .add_yaxis("直播-单流", [66.3, 4.92, 9.91, 175, 19.9, 21.43, 22.76])
    .add_yaxis("直播-合图", [47.6, 3.2, 2.83, 50, 7.33, 7.83, 8.03])
    .add_yaxis("直播-裸数据", [40.4, 3.58, 6.79, 120, 10.62, 8.82, 8.9])
    .add_yaxis("unify-单流", [69.72, 4.86, 5.68, 175, 9.24, 9.3, 9.26])
    .add_yaxis("unify-合图", [42.25, 2.92, 1.7, 50, 7.42, 7.39, 7.8])
    .add_yaxis("unify-裸数据", [46.3, 3.84, 8.7, 120, 8.21, 7.93, 7.41])

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
bar.render("2.8.0_recording_sdk_perf.html")