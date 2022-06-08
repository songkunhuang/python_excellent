import multiprocessing
import time
import os


# 跳舞任务
def dance():
    # 获取进程编号
    print("dance:", os.getpid())

    # 获取当前进程
    print("dance:", multiprocessing.current_process())
    for i in range(10):
        print("dancing...")
# 唱歌任务

# 获取当前进程编号


# 获取