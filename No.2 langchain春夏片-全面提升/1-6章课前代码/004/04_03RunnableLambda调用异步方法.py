import asyncio

from langchain_core.runnables import RunnableLambda


def add(a, b):
    result = a + b
    print("add",result)
    return result

async def sub(a,b):
    result = a - b
    print("sub", result)
    return result
# add(1,1)
# asyncio.run( sub(2,1)) #直接调用异步方法,把协程放入事件循环,并且运行
# runnable1 = RunnableLambda(lambda x :add(x[0],x[1]))
runnable2 = RunnableLambda( lambda x :add(x[0],x[1]), afunc= lambda x :sub(x[0],x[1]))#afunc参数可以传入 异步方法
print(type(runnable2))
# runnable1.invoke((1,2))
# async def fun1():
#     await runnable2.ainvoke((3, 2))#放在函数里用
# asyncio.run(fun1())
#
# asyncio.run(runnable2.ainvoke((4,1)))#直接在外层使用