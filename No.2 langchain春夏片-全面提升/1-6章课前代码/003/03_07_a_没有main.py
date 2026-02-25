import asyncio
from asyncio import Future


async  def task1():
    print("任务 1 开始")
    await asyncio.sleep(0)
    print("任务 1 结束")

async def task2():
    print("任务 2 开始")
    await asyncio.sleep(0)
    print("任务 2 结束")

# await task1()#不能在函数外面 等待await
#协程:async 是异步的意思 def 是定义函数, 组合起来是定义一个 异步函数,但是在python中,异步函数也可以叫做协程

# 事件循环（Event Loop）：要运行异步代码，你需要一个事件循环。asyncio库提供了事件循环的实现。你可以使用asyncio.run()来运行最顶层的异步函数：
#asyncio.run() 创建和管理事件循环：事件循环是异步编程的核心，它负责调度和执行异步任务。asyncio.run 会自动创建一个新的事件循环，然后将传入的协程放入该事件循环中运行。
# 清理资源：当协程执行完毕后，asyncio.run 会自动关闭事件循环，释放相关资源，确保程序的资源管理正确。
# asyncio.run(task1()) #执行完以后才执行下一个
# asyncio.run(task2())
async def event_loop1():
  f =   asyncio.gather(task1(), task2()) #这里没用await 会报错,因为asyncio.gather,返回的还是一个异步
  print("f=",f)
  print("type(f)=", type(f))
  await f
    # 函数用于并发地运行多个协程，不过它本身也是一个异步操作，需要使用
    # await 关键字来等待它完成
# asyncio.run(event_loop1)#报错,不能只传入函数名,需要带()括号 ,ValueError: a coroutine was expected一个协程被期待
asyncio.run(event_loop1())#有括号的才算是协程
# obj1 = task1()#这里报错,最外层不能直接调用异步方法,至少有要有await或者asyncio.run()
asyncio.run( task1())

# 在 asyncio 里，事件循环是核心，它负责调度和执行异步任务。当你调用 asyncio.run() 时，它会创建一个新的事件循环，并且把传入的协程放进这个事件循环中运行。
# 事件循环采用的是单线程的协作式多任务调度机制，这意味着每个协程在执行期间可以主动让出控制权（一般是通过 await 语句），这样事件循环就能去调度其他协程运行。
# await asyncio.sleep(0) 的作用
# await asyncio.sleep(0) 这个语句的作用是让当前协程立即让出控制权给事件循环，从而让事件循环有机会去调度其他等待执行的协程。虽然 asyncio.sleep(0) 不会真正地休眠，但是它会触发协程暂停执行，进而使事件循环能够切换到其他协程。