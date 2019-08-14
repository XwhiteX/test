#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, psutil
from test import time

process_lst = []

def getProcess(pName):
    # 获取当前系统所有进程id列表
    all_pids  = psutil.pids()

    # 遍历所有进程，名称匹配的加入process_lst
    for pid in all_pids:
        p = psutil.Process(pid)
        if (p.name() == pName):
            process_lst.append(p)

    return process_lst

def load_avg():
    # linux
    f = os.popen("uptime | sed 's/,//g' | awk '{print $8,$9,$10}'")

    # mac
    # f = os.popen("uptime | sed 's/,//g' | awk '{print $10,$11,$12}'")
    return f.read().strip()
# 获取进程名位Python的进程对象列表
process_lst = getProcess("htop")

# 获取录制在线数量
def getRecorder():
    # recorder = os.popen("ps -ef | grep AgoraCoreService | grep -v grep | wc -l", 'r')
    # cmd = 'ps -ef | grep AgoraCoreService | grep -v grep | wc -l'
    result = os.popen('ps -ef | grep AgoraCoreService | grep -v grep | wc -l')
    return result.read()

# 获取内存利用率：
# for process_instance in process_lst:
#     print(process_instance.memory_percent())

# # 获取cpu利用率：
# for process_instance in process_lst:
#     process_instance.cpu_percent(None)

# time.sleep(2) 
# for process_instance in process_lst:
#     print(process_instance.cpu_percent(None))

# sys_mem = psutil.virtual_memory().percent
# # 系统内存使用
# print('system mem usage is ',sys_mem)

# # 系统CPU利用率
psutil.cpu_percent(None)

# time.sleep(3)
# print('system cpu usage is: ', psutil.cpu_percent(None))

# load_avg = os.getloadavg()

while True:
    sys_mem = psutil.virtual_memory().percent
    print('system mem usage is: %s%%' %(sys_mem))
    # time.sleep(3)
    # psutil.cpu_percent(None)
    print('system cpu usage is: %s%%' %(psutil.cpu_percent(None)))
    print('system load average is: ', load_avg())
    print('recorder is:', getRecorder())
    time.sleep(2)
