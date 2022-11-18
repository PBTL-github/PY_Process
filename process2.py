from multiprocessing import Process
from time import sleep

# 创建包含参数的进程函数
def emp(sec, name):
    for i in range(3):
        sleep(sec)
        print("my name is %s" % name)


if __name__ == "__main__":
    # # 位置传参
    # p = Process(target=emp, args=(2, "小明"))
    #
    # # 执行
    # p.start()
    #
    # # 回收
    # p.join()

    # 关键字传参
    p = Process(target=emp, kwargs={"name": "xiaoming", "sec": 4})

    p.start()

    p.join()