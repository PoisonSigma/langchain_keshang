#
# 当 Python 执行到 with 语句时，会按以下步骤操作：
# 计算 with 后面的上下文表达式，得到一个上下文管理器对象。
# 调用该上下文管理器对象的 __enter__ 方法。
# 如果使用了 as 关键字，__enter__ 方法的返回值会被赋值给 as 后面的目标变量。
# 执行 with 语句块中的代码。
# 无论代码块是正常执行完毕还是抛出异常，都会调用上下文管理器对象的 __exit__ 方法。
# with 方法 as 一个对象obj
#     obj.改变成员变量的值
#     读取token

class PsDoom:
    def __init__(self):
        self.killed = 0
        self.dead = 0
        self.score = "F"
    def gameBegin(self):
        self.killed = 999
        self.dead = 0
        self.score = "SSS"
    def __enter__(self):#外面的with as执行完,马上就进入enter方法,他返回的结果,给 as后面接受的变量
        print("doom进入地狱")
        print("恶魔开始战栗 \n shake it baby")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("doom通关了,恶魔 devil may cry")
        if exc_type is not None:
            print(f"异常类型：{exc_type}")
            print(f"异常信息：{exc_val}")
            print(f"回溯信息：{exc_tb}")

def IGotLucky():
    return PsDoom()


# with PsDoom() as obj:
with IGotLucky() as cb:
    print("obj=", cb)
    cb.gameBegin()
    print("obj.killed=", cb.killed)
    print("obj.dead=", cb.dead)
    print("obj.score=", cb.score)
    print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
