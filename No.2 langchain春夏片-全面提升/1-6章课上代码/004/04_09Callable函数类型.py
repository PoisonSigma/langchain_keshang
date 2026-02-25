from collections.abc import Callable

#用来定义函数类型Callable
#[]里面第一个中括号,是传入函数的参数类型是2个int,逗号后面的int是返回类型
# def qian(func: Callable[[int, int], int], a, b):
def qian(func:Callable[[int,int],int]):
    print("qian执行了") #执行了附加的东西
    # func(1,2)
    # func(3, 4)
    # func(a,b)
    return func
def add(a,b)->int:
    result = a + b
    print("add执行",result)
    return result
# add(1,2)
fun1 = qian(add) #这里qian返回了函数add
print(fun1)
fun1(3,3)
qian(add) (3,3)#用这种方式,可以让自己的函数,又去调用别人封装好的东西再调用自己