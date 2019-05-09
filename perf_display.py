#! coding=utf-8
from pyecharts.charts import Bar
from pyecharts import options as opts

bar = (
    Bar()
    .add_xaxis(["cpu(%)", "memory", "网络(Mb)", "在线数量", "load 1min", "load 5min", "load 15min"])
    .add_yaxis("2.3.0", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("2.3.1", [66, 114, 87, 59, 195, 50, 69])
    .add_yaxis("2.2.1", [52, 104, 137, 129, 145, 60, 49])
    .add_yaxis("2.2.2", [50, 124, 147, 139, 135, 77, 59])
    .add_yaxis("2.2.3", [67, 134, 157, 159, 125, 64, 79])
    .add_yaxis("2.2.4", [77, 144, 167, 169, 165, 50, 39])
    .set_global_opts(title_opts=opts.TitleOpts(title="压测性能统计"))
)
bar.render("perf.html")