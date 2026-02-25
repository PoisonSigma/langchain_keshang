from typing import Callable


class Person:

    def __init__(self,func:Callable[[int,int],int],a = 0,b = 0):
        self.func = func
        print("Person创建了对象")
        print("self.func=",self.func)
        self.a = a
        self.b = b

# def add(a,b):
#     result = a+b
#     print("add执行",result)
# p1 = Person(add)
# p1.func(1,2)

def qian(func:Callable[[int,int],int]):

    return Person(func)#这里的返回会给sub使用

@qian
def sub(a,b):
    result = a-b
    print("sub执行",result)
# p2 = sub #这个sub函数名 ,相当于执行了 qian(sub)
# print("p2=",p2)
p3 = qian(sub)
print("p3=",p3)
