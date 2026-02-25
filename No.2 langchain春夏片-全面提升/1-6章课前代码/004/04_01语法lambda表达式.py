from langchain.schema.runnable import RunnableLambda


# 定义一个接受两个参数的函数
def add(a, b):
    return a + b
def add_one(a):
    result = a+1
    print("add_one",result)
    return a+1
# runnable1 = RunnableLambda( add_one)
runnable1 = RunnableLambda(lambda a :add_one(a))
runnable1.invoke(2)
runnable1.invoke(4)
# (a,b) = (1,3)
# print(a)
# runnable2 = RunnableLambda(lambda (a,b): add(a,b)) #报错,lambda表达式不能用元组解构作为参数
runnable2 = RunnableLambda(lambda a: add(a[0],a[1]))

runnable2.invoke(input=(2,2))

#
# # 创建一个 RunnableLambda 对象，使用 lambda 函数包装 add_numbers
# add_runnable = RunnableLambda(lambda x: add_numbers(x[0], x[1]))
#
# # 调用 RunnableLambda
# result = add_runnable.invoke((2, 3))
# print(result)

# fun1 = lambda a: a+1 #定义一个lambda表达式 ,传入a是参数,冒号:右边是运行的表达式
# result = fun1(2) #调用lambda
# print(result)
# def add3(a,b):
#     result = a+b
#     print("add3",result)
#
# add3(1,2)
#
# add4 = lambda x:add3(x[0],x[1])
# add4((2,2))#传入元组
#
# add5 = lambda a,b:add3(a,b) #lambda表达式 左边2个参数,a和b,冒号右边是表达式
# add5(3,3)