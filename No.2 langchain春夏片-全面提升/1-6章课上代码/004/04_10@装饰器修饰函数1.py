# 装饰器是一种特殊的函数，它接收一个函数作为参数，
# 被装饰的函数名,会在第一次执行@qian的时候保存 qian函数执行结果

from collections.abc import Callable
def qian(func:Callable[[int,int],int]):
    print("qian执行了========================>") #执行了附加的东西
    return func
@qian # qian(add) #只有再装饰器修饰以后才会运行一次qian(add),后面再直接用add,等于直接调用过qian的返回值func
def add(a,b)->int:
    result = a + b
    print("add执行",result)
    return result
# qian(add) #这个等价于上面的@qian
# fun1 = qian(add)
# print(fun1)
# print(type(fun1))
# fun1(1,2)
# add(1,2)
# p1 = add #返回的是函数地址,函数名
# print(p1)
# print(type(p1))


# p1(1,2)#有括号才算调用
#后面的add,是之前第一次@qian,返回的结果func地址保存给了add
add(1,2)#有括号才算调用,但是这里的add,是执行了qian(add)再返回add函数的调用地址,再调用(1,2)
add(3,4)

