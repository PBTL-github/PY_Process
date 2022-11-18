# 导入模块
import multiprocessing
from time import sleep


# 创建进程执行的函数
def fun():
    print("子进程函数开始执行...")
    # 睡眠模拟程序执行
    sleep(2)
    print("子进程函数执行完成...")


# windows 系统下 必须把子进程相关代码放入if   linux不用
if __name__ == "__main__":
    # 创建子进程对象
    p = multiprocessing.Process(target=fun)

    # 启动子进程， 进程诞生并执行fun函数
    p.start()

    # 主进程执行模拟
    print("主进程开始执行...")
    sleep(5)
    print("主进程执行完成...")

    # 回收
    p.join()
