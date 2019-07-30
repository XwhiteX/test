import plotly.offline as pltoff
import plotly.graph_objs as go

def line_plots(name="line_plots.html"):
    dataset = {
        'cpu': [],
        'memory' : [],
        'load' : [],
        'online' : []
    }
    with open('/Users/yueli/Desktop/linux_share/2.8.0_stable_perf/perf/com/health_check_case1_cpp_mix_com.txt') as f:
        i = 0
        for line in f:
            items = line.split()
            dataset['cpu'].append(i)
            dataset['memory'].append()