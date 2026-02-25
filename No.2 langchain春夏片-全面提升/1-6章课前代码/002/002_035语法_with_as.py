#
# 当 Python 执行到 with 语句时，会按以下步骤操作：
# 计算 with 后面的上下文表达式，得到一个上下文管理器对象。
# 调用该上下文管理器对象的 __enter__ 方法。
# 如果使用了 as 关键字，__enter__ 方法的返回值会被赋值给 as 后面的目标变量。
# 执行 with 语句块中的代码。
# 无论代码块是正常执行完毕还是抛出异常，都会调用上下文管理器对象的 __exit__ 方法。
class PsDoom:
    def __init__(self):
        self.killed = 0
        self.dead = 0
        self.score = "F"
        # __enter__
        # 方法的返回值
        # Python
        # 要求上下文管理器的
        # __enter__
        # # 方法必须返回一个对象，该对象会被赋值给
        # # with... as ... 中的目标变量（即 cb）。如果 __enter__ 没有显式返回值，默认返回 None。
    def gameBegin(self):
        self.killed = 999
        self.dead = 0
        self.score = "SSS"
    def __enter__(self): #enter的返回值会赋值给 as 后面的对象
        print(" doom进入地狱")
        return self #在这里显示返回自己本身,这样外面 with as的时候就能接收到对象了
    def __exit__(self, exc_type, exc_val, exc_tb):#代码块执行完以后,最后执行
        print("demon shake恶魔瑟瑟发抖")
        if exc_type is not None:
            print(f"异常类型：{exc_type}")
            print(f"异常信息：{exc_val}")
            print(f"回溯信息：{exc_tb}")
        return self  # 返回 True 表示忽略异常

with PsDoom() as cb:
    cb.gameBegin()
    print("cd=",cb)
    print(cb.dead)
    print(cb.killed)
    print(cb.score)

#
# def startGame()->PsDoom:
#     print("开始游戏")
#     return PsDoom()
#
# with startGame()as cb:
#     cb.gameBegin()
#     print("cd=",cb)
#     print(cb.dead)
#     print(cb.killed)
#     print(cb.score)

