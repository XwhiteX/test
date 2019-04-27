#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# import json, os, time, psutil, netifaces
import json, os, time, psutil

 
def GetCPUorDiskTemper(type='Core'):
    	dict_cpu_temp = {}
	if hasattr(psutil, "sensors_temperatures"):
		temps = psutil.sensors_temperatures()
	else:
		temps = {}
	cpu_each = []
	names = list(temps.keys())
	for name in names:
		if name in temps:
			for entry in temps[name]:
				if type in entry.label:
					dict_cpu_temp[entry.label] = entry.current
					cpu_each.append(dict_cpu_temp[entry.label])
	cpu_top = sorted(dict_cpu_temp.items(),key=lambda d:d[0])[0][1]
	return {"cpu_top":cpu_top,"cpu_each":cpu_each}
 
def GetCPUInfo():
	cpu_t = GetCPUorDiskTemper()["cpu_each"]
	cpu_num = int(os.popen("cat /proc/cpuinfo| grep 'physical id'| sort| uniq| wc -l").readline().strip())
	numb = os.popen("cat /proc/cpuinfo| grep 'cpu cores'| uniq").readline()
	cpucore_num = int(numb[12:-1])
	cpu_u = psutil.cpu_percent(percpu=True,interval=1)
	cpu = []
	cpu1 = {}
	list = {}
	y = 1
	z = 0
	data = []
	for i in range(0,len(cpu_u)):
		list = {"corename":"Core "+str(z),"cpu_u":cpu_u[i],"cpu_t":cpu_t[i]}
		z = z + 1
		data.append(list)
		if i+1 == cpucore_num*y:
			cpu1["data"] = data
			cpu1["cpuname"] = "cpu "+str(y-1)
			y = y + 1
			cpu.append(cpu1)
			cpu1 = {}
			data = []
			z = 0
	return cpu
 
# def GetNetwork():
# 	net = []
# 	for i in range(1,len(netifaces.interfaces())):
# 		netname = str(netifaces.interfaces()[i])
# 		bytes_sent = int(psutil.net_io_counters(pernic=True)[netname][0])
# 		bytes_recv = int(psutil.net_io_counters(pernic=True)[netname][1])
# 		eth_status = os.popen('sudo ethtool '+netname).readlines()[-1][16:-1]
# 		x = {"name":netname,"eth_status":eth_status,"bytes_sent":bytes_sent,"bytes_recv":bytes_recv}
# 		net.append(x)
# 	return net
total = 0
used = 0
disk_partitions = psutil.disk_partitions(all=False)
for i in range(0,len(disk_partitions)):
	partition = disk_partitions[i][1]
	total_each = psutil.disk_usage(partition)[0]
	total = total + total_each
	used_each = psutil.disk_usage(partition)[1]
	used = used + used_each
disk_u = used/float(total)*100
cpu_u = psutil.cpu_percent(1)
cpu_t = GetCPUorDiskTemper()["cpu_top"]
memory_u = psutil.virtual_memory().percent
boot_time = psutil.boot_time()
runtime = os.popen('cat /proc/uptime').readlines()[0].split(" ")[0]
# data = {"a":{"disku":disk_u,"memu":memory_u,"cpuu":cpu_u,"cput":cpu_t,"boot_time":boot_time,\
		# "runtime":runtime},"b":GetNetwork(),"c":GetCPUInfo()}
data = {"a":{"disku":disk_u,"memu":memory_u,"cpuu":cpu_u,"cput":cpu_t,"boot_time":boot_time,\
		"runtime":runtime},"c":GetCPUInfo()}
print(data)