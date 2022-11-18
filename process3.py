from multiprocessing import Process
import time


# 创建函数
def fun():
    for i in range(3):
        # 打印时间
        print(time.ctime())
        time.sleep(2)


if __name__ == "__main__":
    p = Process(target=fun)

    # 设置True 子进程随父进程的退出而退出  要在start之前设置
    p.daemon = True
    p.start()

    # 查看进程的名字
    print(p.name)
    # 查看进程的id
    print(p.pid)
    # 查看进程的存活状态
    print(p.is_alive())


"""
os.getpid    获取子进程
os.getppid   获取父进程
sys.exit     退出进程
"""