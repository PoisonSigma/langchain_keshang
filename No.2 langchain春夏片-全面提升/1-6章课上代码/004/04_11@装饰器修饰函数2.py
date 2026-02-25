

from collections.abc import Callable
class RullableLawada:
    def __init__(self,func:Callable[[int,int],int]):
        self.func = func
        print("软啦布拉乌达创建成功=======================>")
    def invoke(self,a,b):
        self.func(a,b)
        print("invoke执行 id=",id(self))
def qian(func:Callable[[int,int],int]):
    print("qian执行了=======>") #执行了附加的东西
    return RullableLawada(func)
@qian
def tamenchongworengbaba(a,b):
    result = a + b
    print("tamenchongworengbaba他们冲我扔粑粑,我拿粑粑做蛋挞", result)
    return result
tamenchongworengbaba.invoke(3,4)
tamenchongworengbaba.invoke(3,4)
@qian # qian(add)
def add(a, b)->int:
    result = a + b
    print("add执行",result)
    return result

def sub(a,b):
    result = a - b
    print("sub执行",result)
    return  result


# r2 = RullableLawada(sub)
# print("r2类型",type(r2))
# r2.func(1,2)
add.invoke(10, 1) #这个add已经再第一次@qian时qian函数返回了RullableLawada()对象,并且保存在add中
add.invoke(10, 2)
# qian(add)#这样才是调用qian,相当于@qian
# qian(add)
#add(1,2)#报错,add已经不是普通的函数add,这里的add已经变成了qian()的返回值,是对象,只在上面@qian的时候返回一次对象


