import time  # time.sleep(睡眠的秒数)
import asyncio

# if __name__ == '__main__':
#     print('hello')
#     time.sleep(3)   # 让当前的线程处于阻塞状态，CPU不工作
#     print('world')


# input() 程序也是阻塞状态
# request.get() 网络请求返回数据之前，程序也是处于阻塞状态
# 一般情况下当程序初于IO操作时，程序都是处于阻塞状态

# 协程，当程序遇见IO操作时，选择性的切换到其他任务上
# 微观上一个一个执行，有条件切换，宏观上多个任务同时执行
# 多任务异步

# 这一切都是在单线程条件下


# async def func():   # 协程异步函数
#     print('天龙八部')


# if __name__ == '__main__':
#     g = func()      # 得到一个协程对象，原函数不会运行
#     asyncio.run(g)      # 协程对象运行需要一个ａｓｙｎｃｉｏ模块的支持

# async def func1():   
#     print('天龙八部')
#     # time.sleep(2)       # 当程序出现同步操作时，异步就切断了，不能这么睡
#     await asyncio.sleep(2)      # 要这么睡，异步操作的代码
#     print('天龙八部')


# async def func2():   
#     print('射雕英雄传')
#     # time.sleep(3)
#     await asyncio.sleep(3)
#     print('射雕英雄传')


# async def func3():   
#     print('神雕侠侣')
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print('神雕侠侣')


# if __name__ == '__main__':        # 主函数里东西太多了
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()

#     tasks = [f1, f2, f3]        # 将三个任务放入列表

#     t1 = time.time()
#     # 一次性启动多个任务（协程）
#     asyncio.run(asyncio.wait(tasks))

#     t2 = time.time()
#     print(t2 - t1)      #记录程序运行时间


async def func1():   
    print('天龙八部')
    await asyncio.sleep(2)      
    print('天龙八部')


async def func2():   
    print('射雕英雄传')
    await asyncio.sleep(3)
    print('射雕英雄传')


async def func3():   
    print('神雕侠侣')
    await asyncio.sleep(4)
    print('神雕侠侣')


async def main():
    tasks = [func1(), func2(), func3()]
    await asyncio.wait(tasks)       # await挂起操作放在协程对象前面



if __name__ == '__main__':
    t1 = time.time()

    asyncio.run(main())

    t2 = time.time()
    print(t2 - t1)      #记录程序运行时间