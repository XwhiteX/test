#coding=utf-8

import logging
import psutil
import os

log_filename = "logging.txt"

log_format = '[%(asctime)s] %(message)s'

logging.basicConfig(format=log_format, datefmt='%Y-%m-%d %H:%M:%S %p', level=logging.DEBUG, filename=log_filename, filemode='w')

logging.debug('日志输出！')

p1 = psutil.Process(os.getpid())

print('直接打印内存占用：'+ (str)(psutil.virtual_memory))

print('获取内存占用率：'+ (str)(psutil.virtual_memory().percent)+ '%')

print('打印CPU占用率：'+ (str)(psutil.cpu_percent(0))+'%')

print('打印该进程CPU占用率：'+ (str)(p1.cpu_percent(None))+ '%')

print(p1.memory_percent)

print("percent: %.2f%%" % (p1.memory_percent()))
