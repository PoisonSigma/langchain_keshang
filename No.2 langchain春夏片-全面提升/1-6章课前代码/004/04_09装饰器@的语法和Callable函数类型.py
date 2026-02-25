from typing import Union, Callable

#Callable[[int,int],int] 类型,第一个[int,int],代表函数传入的参数类型是2个int,后面逗号,int是返回类型
def pschain(func: Callable[[int,int],int],a:int,b:int):
    func(a,b)

def add(a,b):
    result = a+b
    print("add执行",result)
pschain(add,1,1)#这样可以调用给函数传入函数




#
# def chain(
#     func:
# ) ->
#
#     return RunnableLambda(func)