import re
import sys
from pyecharts.charts import Bar,Line
from pyecharts import options as opts
import logging
import logging.config


logging.basicConfig(
    format='%(name)s:%(lineno)d - %(levelname)s - %(message)s',
    level=logging.DEBUG)



checklist = ['cpu_percent', 'percent', 'bps_rx', 'min1', 'min5', 'min15', 'online']
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
        # sum_data = 0
        # for item in calculat(check):
        #     sum_data += float(item)
        # avg_data = '%.2f' % (sum_data / float(len(calculat(check)))) # 四舍五入取后两位

        if check == 'online':
            online = calculat(check)
        elif check == 'cpu_percent':
            cpu_percent = calculat(check)
        elif check == 'percent':
            mem = calculat(check)
        # elif check == 'bps_rx':
        #     net = '%.2f' % (float(calculat(check)) / 1000000 / 8) # 带宽换算，从 bps 换算到 MB/s
        else:
            load = calculat(check)
            if check == 'min1':
                min1 = calculat(check)
            elif check == 'min5':
                min5 = calculat(check)
            else:
                min15 = calculat(check)
    return cpu_percent, mem,  min1, min5, min15, online


# 折线图

cpu = avg(checklist)[0]
mem = avg(checklist)[1]
load_min1 = avg(checklist)[2]
load_min5 = avg(checklist)[3]
load_min15 = avg(checklist)[4]
perf_data = list(range(len(calculat("online"))))

(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=perf_data)
    .add_yaxis(
        series_name="CPU",
        y_axis=cpu,
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="mix", name="最小值"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .add_yaxis(
        series_name="Load min1",
        y_axis=load_min1,
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="mix", name="最小值"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .add_yaxis(
        series_name="Load min5",
        y_axis=load_min5,
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="mix", name="最小值"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .add_yaxis(
        series_name="Load min15",
        y_axis=load_min15,
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="mix", name="最小值"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .add_yaxis(
        series_name="内存",
        y_axis=mem,
        # markpoint_opts=opts.MarkPointOpts(
        #     data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
        # ),
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
            ]
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="性能曲线", subtitle="xxx版本"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("temperature_change_line_chart.html")
)