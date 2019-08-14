import os
import re

def eachFile(filpath):
    pathDir = os.listdir(filpath)
    return pathDir

def cpufile(name):
    fopen = open(name,'r')
    for lines in fopen.readlines():
        lines = lines.replace("\n", "").split(",")
        if 'cpu_percent' in str(lines):
            print(lines)
    fopen.close()

def memoryfile(name):
    fopen = open(name,'r')
    for lines in fopen.readlines():
        lines = lines.replace("\n", "").split(",")
        if 'memory' in str(lines):
            print(lines)

        # if 'online' in str(lines):
        #     # result = re.match('.*(\d)', str(lines))
        #     result = re.search(r"(?P<percent>\d+)", str(lines))
        #     results = (result.group('percent'))
        #     print(results)
    fopen.close()

def loadfile(name):
    fopen = open(name,'r')
    for lines in fopen.readlines():
        lines = lines.replace("\n", "").split(",")
        if 'load' in str(lines):
            print(lines)
        # if 'online' in str(lines):
        #     # result = re.match('.*(\d)', str(lines))
        #     result = re.search(r"(?P<load>\d+)", str(lines))
        #     results = (result.group('load'))
        #     print(results)
    fopen.close()

def onlinefile(name):
    fopen = open(name,'r')
    for lines in fopen.readlines():
        lines = lines.replace("\n", "").split(",")
        # result = re.match('.*?(\d.*\d).*', lines)
        # t = (result.group(1))
        if 'online' in str(lines):
            # result = re.match('.*(\d)', str(lines))
            result = re.search(r"(?P<online>\d+)", str(lines))
            results = (result.group('online'))
            print(results)

        # if 'online' in str(lines):
        #     print(lines)
    fopen.close()

# '.*?(\d.*\d).*'
# ["online_cnt: [{'online': 50}]"]


filePath = "/Users/yueli/Desktop/linux_share/2.8.0_stable_perf/perf/com_rerun/"
pathDir = eachFile(filePath)
for allDir in pathDir:
    child = "/Users/yueli/Desktop/linux_share/2.8.0_stable_perf/perf/com_rerun/" + '/' + allDir
    print('\n', child)
    cpufile(child)
    memoryfile(child)
    loadfile(child)
    onlinefile(child)