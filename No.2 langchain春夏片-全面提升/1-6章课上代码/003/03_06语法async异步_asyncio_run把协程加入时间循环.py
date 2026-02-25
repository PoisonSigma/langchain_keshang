# 事件循环（Event Loop）：要运行异步代码，你需要一个事件循环。asyncio库提供了事件循环的实现。你可以使用asyncio.run()来运行最顶层的异步函数：
#asyncio.run() 创建和管理事件循环：事件循环是异步编程的核心，它负责调度和执行异步任务。asyncio.run 会自动创建一个新的事件循环，然后将传入的协程放入该事件循环中运行。
# 清理资源：当协程执行完毕后，asyncio.run 会自动关闭事件循环，释放相关资源，确保程序的资源管理正确。
import asyncio

#协程,是在单线程中的一个一小段任务,又叫为微线程
async def fun1():
    print("fun1开始了")
    # await asyncio.sleep(0)
    print("fun1结束了")

async def fun2():
    print("fun2开始了")
    # await asyncio.sleep(0) #这里没有调用gather无法并发执行,用await也不会跳到fun2
    print("fun2结束了")
print("1 铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

asyncio.run(fun1())#把协程,就是异步方法,加入到事假内循环中,执行结束以后会清楚资源
print("2 铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
#这个run,是时间循环结束以后才向下执行
asyncio.run(fun2())#把协程,就是异步方法,加入到事件内循环中,一般asyncio.run在最顶层
print("3 铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")


