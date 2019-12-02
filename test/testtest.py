# -*- coding:utf-8 -*-
import re
import sys
checklist = ['Write', 'Read']
file_path = '/Users/yueli/Desktop/tiotest.txt'
# file_path = sys.argv[1] # 文件地址


def calculat(check_op):
    with open(file_path, 'r') as f:
        data_list = []
        for line in f.readlines():
            b = re.sub("[^a-zA-Z0-9\s.\w$]", '', str(line)) # 匹配数字、字母、英文{dot.}、下滑线
            list_b = b.strip().split(" ") # 把列表中的前后空格和换行符去掉
            price = [x.strip() for x in list_b if x.strip() != '']
            if check_op in price:
                data = price.index(check_op) + 5
                data_list.append(price[data])
        return data_list
        
def result(check_list):
    for check in checklist:
        if check == 'Write':
            write = calculat(check)
        elif check == 'Read':
            read = calculat(check)
    return write, read

for i in range(len(result(checklist)[0])):
    print('Write is: %s \t' % result(checklist)[0][i]  + 'Read is: %s' %result(checklist)[1][i])



    

