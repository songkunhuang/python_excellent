import multiprocessing
import time


# 跳舞任务
def dance():
    for i in range(5):
        print("Dancing...\n")
        time.sleep(0.2)


# 唱歌任务
def sing():
    for i in range(5):
        print("Sing...\n")
        time.sleep(0.2)

#  创建跳舞的子进程
#  group：
#  target：
#  name:


dance_process = multiprocessing.Process(target=dance, name='P1-Dance Process')
sing_process = multiprocessing.Process(target=sing, name='P2-Sing Process')

#  启动子进程执行对应任务
if __name__ == '__main__':
    dance_process.start()
    sing_process.start()


