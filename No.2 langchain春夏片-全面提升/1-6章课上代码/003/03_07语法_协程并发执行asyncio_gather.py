import asyncio
from asyncio import Future

from langchain_community.llms.tongyi import astream_generate_with_retry


async  def gasGuan1():
    print("蛋清气体重力加速系统冲天瞄准↑")
    # await asyncio.sleep(0)
    print("重力加速,深蹲的时候,变成倒立,变成肩膀中束锻炼↑")

async def gasGuan2():
    print("蛋清气体重力加速系统冲地面瞄准↓")
    # await asyncio.sleep(0)
    print("平时蹲100,力量举130,人间大炮一级准备:蹲200↓")
async def fun3():
    # 异步方法要放在await里面,await必须放在async,这种协程,又叫异步方法里面
    # f =  asyncio.gather(gasGuan1(), gasGuan2()) #Future类型
    # await f
    # f:asyncio.Future = asyncio.gather(gasGuan1(), gasGuan2())
    #gather里面要的参数是协程,不能是普通函数
    # f2:Future = asyncio.gather(gasGuan1(), gasGuan2())
    #gather本身是异步的,所以也要await
     await asyncio.gather(gasGuan1(),gasGuan2())
    # await asyncio.gather(gasGuan1(), gasGuan2())
asyncio.run(fun3())
