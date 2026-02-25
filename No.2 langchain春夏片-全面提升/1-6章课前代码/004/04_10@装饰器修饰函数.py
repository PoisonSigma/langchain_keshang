# 装饰器是一种特殊的函数，它接收一个函数作为参数，
#  在调用@ 装饰器的时候把返回结果给 被装饰的函数 ,例如返回新的函数或者类的对象
# Python 会自动把被装饰的函数作为参数传递给装饰器函数。

from typing import Callable


def pschain(func: Callable[[int,int],int]):   #pschain 函数接收 add 函数作为参数。
    print("pschain函数执行了,并且执行了额外方法")
    def dofunc(a,b):  #pschain 函数内部定义了一个新的函数 dofunc，
        return func(a,b)#它会调用原始的 add 函数。
#pschain 函数返回 dofunc 函数，并将其赋值给 add。
    return dofunc
    # func(a,b)
#@pschain 装饰 add 函数时，会把add 函数作为参数传递给 pschain
@pschain   #这里已经代表执行了pschain(add)
def add(a,b):
    result = a+b
    print("add执行",result)
# pschain(add) #等价于上面@pschain

add(3,3)


