#-*- encoding:UTF-8 -*-
import psutil

def getPidByName(Str):
    pids = psutil.process_iter()
    pidList = []
    for pid in pids:
        if pid.name() == Str:
            pidList.append(pid.pid)
            # print('pid is:',pidList)
    print('pid is:',pidList)
    # return pidList


if __name__ == '__main__':
    pid = getPidByName('ssh')
    # print('ssh pid is:',pid)