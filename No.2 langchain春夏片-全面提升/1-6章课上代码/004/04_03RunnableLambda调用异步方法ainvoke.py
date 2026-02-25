import asyncio

from langchain_core.runnables import RunnableLambda

#
def add(a,b):
    result = a + b
    print("add()=", result)
    return (result,1)#这里是为了返回元组,可以连续的invoke

# add(1,1)
async def sub(a,b):
    result = a - b
    print("异步方法执行sub()=", result)
    return (result,1)#这里是为了返回元组,可以连续的invoke
# sub(1,1)#不能直接调用
# asyncio.run( sub(10,1)) #创建一个事件循环,并且把异步方法放进去,开始执行

# async def sub_run(): #把异步方法放到异步方法里面await等待
#     await sub(10,1)
# asyncio.run(sub_run())#再调用异步方法

# runable1 = RunnableLambda(lambda x:add(x[0],x[1]))
# runable1.invoke((1,1))#同步的输入输出
# chain =  runable1 | runable1  #RunnableSerializable ,函数被RunnableLambda包裹之后,可以使用管道操作符\
# result = chain.invoke((1,1))
# print("result=",result)
# runable1.ainvoke((1,1))
runable2 = RunnableLambda(lambda x:add(x[0],x[1]),afunc= lambda x:sub(x[0],x[1]))

# chain = runable1 | runable1
async def run2():
    await runable2.ainvoke((10,9))#调用runnable对象里面的异步方法
# asyncio.run(run2())
asyncio.run( (runable2 | runable2).ainvoke((10,9))) #连续调用2次ainvoke
#ainvoke的输入,是传入的参数,输出是 函数的return返回值
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

runable2.invoke((3,3))