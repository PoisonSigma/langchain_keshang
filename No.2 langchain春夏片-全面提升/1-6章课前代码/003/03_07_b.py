import asyncio

async def async_function():
    print("这是一个异步函数")
    await asyncio.sleep(1)#等待睡眠
    print("异步函数执行结束")

# 调用协程函数但不使用 await
# async_function()# RuntimeWarning: coroutine 'async_function' was never awaited
# #警告,值创建了协程对象,但是没有等待
# print(f"返回的是协程对象: {coroutine_obj}")
asyncio.run(async_function())#可以把异步函数放到 事件循环中循环中