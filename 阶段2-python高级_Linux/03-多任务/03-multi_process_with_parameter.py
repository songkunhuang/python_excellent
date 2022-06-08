import multiprocessing
import time


# function with parameter
def task(count):
    for i in range(count):
        print(i, "task is running...")
        time.sleep(0.2)
    else:
        print("task completed.")


if __name__ == '__main__':

    # transfer parameter with args
    sub_process = multiprocessing.Process(target=task, args=(5, ))
    sub_process.start()

    # transfer parameter with kwargs
    sub_process = multiprocessing.Process(target=task, kwargs={'count': 3})
    sub_process.start()
