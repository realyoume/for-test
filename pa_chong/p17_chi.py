# 线程池 一次性开辟多个线程 用户直接给线程池提交任务 内部的调度交给线程池来管

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def func(name):
    for i in range(10):
        print(f"线程{name}", i)


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(func, name=i)   # submit 给线程池提交任务

    print('ok')