# -*- coding:utf-8 -*-

file_path = '/Users/kkk/Desktop/health_check_case1_cpp_single_live.txt'
checklist = ['cpu_percent', 'percent', 'bps_rx', 'min1', 'min5', 'min15']

def calculat(check_op):
    with open(file_path, 'r') as f:
        data_list = []
        for line in f.readlines():
            list_a = line.strip().split(",") # 把数据按照逗号分隔开
            list_b = [x.strip() for x in list_a] # 把列表中的前后空格和换行符去掉
            if check_op in list_b:
                data = list_b.index(check_op) + 1
                data_list.append(list_b[data])
        return data_list
    

def avg(check_list):
    for check in checklist:
        sum_data = 0
        for item in calculat(check):
            sum_data += float(item)
        avg_data = '%.2f' % (sum_data / float(len(calculat(check)))) # 四舍五入取后两位

        if check == 'cpu_percent':
            print('performance machine\'s CPU use percent is: ' + str(avg_data) + '%\n')
        elif check == 'percent':
            print('performance machine\'s MEM use percent is: ' + str(avg_data) + '%\n')
        elif check == 'bps_rx': # 带宽换算还需要重新计算，目前拿到的是bps_rx
            print('performance machine\'s NETWORK use is: ' + str(avg_data) + ' bps_rx\n')
        else:
            print('performance machine\'s system load average ' + check + 'is: ' + str(avg_data) + '\n')

avg(checklist)


        # a = calculat(check)
        # sum_data = 0
        # for item in a:
        #     sum_data += float(item)
        # avg_data = sum_data / float(len(a))
        # print('performance machine\'s ' + check + ' is:\n' + str(avg_data) + '\n')



# def avg(file_path, check_list):
#     with open(file_path, 'r') as f:
#         data_list = []
#         check_data = check_list
#
#         for line in f.readlines():
#             list_a = line.strip().split(",")
#             list_b = [x.strip() for x in list_a]
#
#             if check_data in list_b:
#                 data = list_b.index(check_data) + 1
#                 # print(data)
#                 data_list.append(list_b[data])
#         sum_data = 0
#         for item in data_list:
#             sum_data += float(item)
#         # print(sum)
#         avg_data = sum_data / float(len(data_list))
#         print('performance machine\'s ' + check_data + ' is:\n' + str(avg_data))

# avg(file_path, checklist)
# print(type(checklist))

# 获取平均数
# def Get_Average(list):
#     sum = 0
#     for item in list:
#         sum += float(item)
#     return sum / float(len(list))
#
#
# # 最大数
# def Get_Max(list):
#     return max(list)
#
#
# # 最小数
# def Get_Min(list):
#     return min(list)
#
#
# # 极差
# def Get_Range(list):
#     return max(list) - min(list)
#
#
# # 中位数
# def get_median(data):
#     data = sorted(data)
#     size = len(data)
#     if size % 2 == 0:
#         # 判断列表长度为偶数
#         median = (data[size // 2] + data[size // 2 - 1]) / 2
#     if size % 2 == 1:
#         # 判断列表长度为奇数
#         median = data[(size - 1) // 2]
#     return median
#
#
# # 众数(返回多个众数的平均值)
# def Get_Most(list):
#     most = []
#     item_num = dict((item, list.count(item))
#                     for item in list)
#     for k, v in item_num.items():
#         if v == max(item_num.values()):
#             most.append(k)
#     return sum(most) / len(most)

# for line in f:
# result.append(list(line.strip('cpu_percent').split(',')[0]))

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
