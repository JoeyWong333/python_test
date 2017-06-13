#!/usr/bin/env python
# coding:utf-8

"""
@author:Joey
create:2017-0613
"""

#使用psutil 系统进程监控
import psutil,datetime

def systemInfo():
    print("cpu状态：" + str(psutil.cpu_stats()))
    print("cpu的逻辑个数：" + str(psutil.cpu_count()))
    print("cpu的物理数量：" + str(psutil.cpu_count( logical=False)))
    print("cpu的整个信息:" + str(psutil.cpu_times()))
    print("cpu的IDLE信息：" + str(psutil.cpu_times().idle))
    print("内存的完整信息:" + str(psutil.virtual_memory()))
    mem = psutil.virtual_memory()
    print("内存总数:" + str(mem.total))
    print("空闲的内存信息：" + str(mem.free))
    print("swap分区信息：" + str(psutil.swap_memory()))
    print("D盘利用率：" + str(psutil.disk_usage('D:/')))
    print("IO信息：" + str(psutil.disk_io_counters()))
    print("磁盘的完整信息:" + str(psutil.disk_partitions()))
    print("分区的状态：" + str(psutil.disk_usage("/")))
    print("硬盘IO总个数："+str(psutil.disk_io_counters()))
    print("单个分区IO个数："+ str(psutil.disk_io_counters(perdisk=True)))
    print("网络总IO信息:"+str(psutil.net_io_counters()))
    print("输出网络每个接口信息："+str(psutil.net_io_counters(pernic=True)))
    print("用户登录信息："+str(psutil.users()))
    #psutil.boot_time()  # 以linux时间格式返回
    print("开机时间："+str(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H: %M: %S")))  # 转换成自然时间格

    print("==========================================系统进程管理===========================================")
    print("所有进程的PID:"+str(psutil.pids())) #方法获取所有进程的PID,
    #psutil.Process(2423) 单个进程的名称, 路径状态等
    print("查看系统全部进程："+str(psutil.pids()))

    #查看单个进程
    p = psutil.Process(3172)
    print("3172进程名:"+str(p.name()))  # 进程名
    #p.exe()  # 进程的bin路径
    #p.cwd()  # 进程的工作目录绝对路径
    print(psutil.AccessDenied(pid=3172, name='Weibo.exe'))
    print("进程状态："+str(p.status()))  # 进程状态
    print("进程创建时间:"+str(p.create_time()))  # 进程创建时间
    print("进程的cpu时间信息,包括user,system两个cpu信息:"+str(p.cpu_times()))  # 进程的cpu时间信息,包括user,system两个cpu信息
    print("进程内存利用率:"+str(p.memory_percent()))  # 进程内存利用率
    print("进程内存rss,vms信息:"+str(p.memory_info())) # 进程内存rss,vms信息
    print("进程的IO信息,包括读写IO数字及参数:"+str(p.io_counters()))  # 进程的IO信息,包括读写IO数字及参数
    #print(p.connections())  #0 返回进程列表
    # p.uids()  # 进程uid信息
    # p.gids()  # 进程的gid信息
    print("程开启的线程数:"+str(p.num_threads()))  # 进程开启的线程数
    #听过psutil的Popen方法启动应用程序，可以跟踪程序的相关信息
    # from subprocess import PIPE
    # p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
    # print(p.name())
    # print(p.username())

systemInfo()

