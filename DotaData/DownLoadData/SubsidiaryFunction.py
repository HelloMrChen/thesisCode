# encoding=utf-8
#本文件用来存放辅助功能函数

import psutil
p = psutil.Process(pid)
p.suspend()   #挂起进程
# p.resume()    #恢复进程