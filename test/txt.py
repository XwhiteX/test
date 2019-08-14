import re
dataset = {
    'cpu': [],
    'memory': [],
    'load': [],
    'online': []
}
with open("/Users/kkk/Downloads/perf/com/health_check_case1_cpp_mix_com.txt") as f:
    i = 0
    for line in f:
        items = line.split()
        # cpu = dataset['cpu'].append(items["cpu", 1])
        cpu = re.split(r'cpu_percent', line)
        print cpu
