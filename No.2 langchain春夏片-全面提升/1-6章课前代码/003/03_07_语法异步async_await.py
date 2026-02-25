import asyncio

# 直接在顶层代码中使用await是语法错误。你必须在异步函数内部使用await。
# 如果你需要在非异步函数中调用异步函数的结果，你可以使用.run_until_complete()
# 方法或者将结果赋值给一个变量
async def task1():
    print("任务 1 开始")
    # await asyncio.sleep(2)
    print("任务 1 结束")

async def task2():
    print("任务 2 开始")
    await asyncio.sleep(1)
    print("任务 2 结束")

async def main():
    print("主函数开始")
    # 创建任务
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())

    # 等待所有任务完成
    await asyncio.gather(task_1, task_2)
    print("主函数结束")

# 运行异步程序
asyncio.run(main())