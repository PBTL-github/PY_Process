from multiprocessing import Process
import time, os, sys


# 创建多个函数
def fun1():
    time.sleep(2)
    print("看书")
    print(os.getppid(), "---", os.getpid())


def fun2():
    time.sleep(2)
    print("听歌")
    print(os.getppid(), "---", os.getpid())


def fun3():
    time.sleep(2)
    print("睡觉")
    print(os.getppid(), "---", os.getpid())


if __name__ == "__main__":
    # 函数列表
    process_list = [fun1, fun2, fun3]
    # 回收列表
    jobs = []

    # 循环执行多个进程
    for fun in process_list:
        p = Process(target=fun)
        jobs.append(p)
        p.start()

    # 循环回收
    for i in jobs:
        i.join()
