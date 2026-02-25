#RunnableLambda 可以把函数封装成Runnable
from langchain_core.runnables import RunnableLambda


def add_one(a):
    result = a+1
    print("add_one=",result)
funx = lambda x :add_one(x)
funx(1)

# runnable1 = RunnableLambda(add_one)#这2种写法效果一样
runnable1 = RunnableLambda(lambda x :add_one(x))#这2种写法效果一样
print(runnable1)
print(type(runnable1))
runnable1.invoke(1)# invoke有输入有输出
runnable1.invoke(2)

def add(a,b):
    result = a + b
    print("add()=", result)
    return result
# add(1,2)
runnable2 = RunnableLambda(lambda x:add(x[0],x[1]))
#多参数,封装成runnable可以用lambda表达式,传入一个元组,再用下标调用函数参数
runnable2.invoke(input = (10,2))



