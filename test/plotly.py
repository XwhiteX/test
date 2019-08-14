def line_plots(name="line_plots.html"):
    dataset = {
        'cpu': [],
        'memory': [],
        'load': [],
        'online': []
    }
    with open("./log.txt") as f:
        i = 0
        for line in f:
            items = line.split()
            dataset['cpu'].append(i)
            dataset['memory'].append(items[0])
            dataset['load'].append(items[1])
            dataset['online'].append(items[2])
            i += 1

    data_g = []
    # 构建 time - rx 数据关系，折线图
    tr_rx = go.Scatter(
        x = dataset['time'],
        y = dataset['rx'],
        name = 'rx')
    data_g.append(tr_rx)

    tr_tx = go.Scatter(
        x = dataset['time'],
        y = dataset['tx'],
        name = 'tx')
    data_g.append(tr_tx)

    tr_util = go.Scatter(
        x = dataset['time'],
        y = dataset['util'],
        name = 'util')
    data_g.append(tr_util)

    # 设置图表布局
    layout = go.Layout(title="Line plots",
        xaxis={'title':'time'}, yaxis={'title':'value'})
    fig = go.Figure(data=data_g, layout=layout)
    # 生成离线html
    pltoff.plot(fig, filename=name)

if __name__=='__main__':
    line_plots()