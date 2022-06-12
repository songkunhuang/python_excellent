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
def sing():
    # 获取当前进程编号
    print("sing:", os.getpid())

    # 获取当前进程
    print("sing current process:", multiprocessing.current_process())


    for i in range(5):
        print("singing...")
        time.sleep(0.2)

# 获取当前进程编号
if __name__ == '__main__':
    # 获取主进程编号
    print("main:", os.getpid())
#     获取主进程
    print("main current process:", multiprocessing.current_process())

    dance_process = multiprocessing.Process(target=dance, name="dance process", group=None)
    sing_process = multiprocessing.Process(target=sing, name="sing process", group=None)

    # 启动子进程
    dance_process.start()
    sing_process.start()