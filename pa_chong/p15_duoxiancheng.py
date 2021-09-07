# 进程 资源单位 工厂
# 线程 执行单位 流水线

from threading import Thread


def func(name):
    for i in range(20):
        print(name, i)


if __name__ == '__main__':
    t1 = Thread(target=func, args=("郭靖",))     # 创建一个新线程并 target 赋予工作
    t1.start()                   # 开始线程
    # for i in range(20):
    #     print('main', i)

    t2 = Thread(target=func, args=("杨过",))     # args 传入参数
    t2.start() 