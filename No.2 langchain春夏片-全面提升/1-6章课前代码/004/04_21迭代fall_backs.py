
from typing import Iterator
from langchain_core.runnables import RunnableGenerator, RunnableLambda

#yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
#执行yield返回 generator生成器,生成器可以被迭代,每次 next获取下一次yield返回的值
def fun1(str1:str):
    print("fun1执行")
    # (str1.find("吃") != -1) || (str1.find("吃") != -1)#注意,python的逻辑或不是||而是or ,&&逻辑与是 and
    if (str1.find("吃") == -1) and (str1.find("金") == -1):#没找到吃,并且没找到金
        yield "你"
        yield "好"
        yield "啊"
        yield "今晚"
        yield "上"
        yield "泡面的"
        yield "钱"
        yield "省下"
        yield "了"
    else:
        print("fun1()找到 金 或者 吃")#一次没迭代,也会向下走

# it1 = fun1() #这里返回的是生成器generator
# print(it1)
# print(type(it1))
# result = next(it1) #返回生成器里面只想的位置,并且指向未知向后移动一个位置
# print(result)
# result = next(it1) #返回生成器里面只想的位置,并且指向未知向后移动一个位置
# print(result)
# for chunk in it1:
#     print("chunk=",chunk)


def error_fun1(str1:str):
    index = str1.find("金卡")
    if index != -1:
        print("error_fun1()有人给金卡,抛出异常")
        raise ValueError("有人给金卡")
    yield "我只能站着死"
    yield "不能跪着活"
def error_fun2(str1:str):
    print("error_fun2执行")
    yield "你在教我做事啊"
    yield "以后不许在我面前说我兄弟坏话"

# 创建主要的可运行对象
# main_runnable = RunnableGenerator(psTransform)#成器函数包装成可运行对象
runnable1 = RunnableLambda(fun1)

# 创建备用的可运行对象
runnable_error1 = RunnableLambda(error_fun1)
runnable_error2 = RunnableLambda(error_fun2)
# 使用 fallbacks 创建新的可运行对象
chain = runnable1.with_fallbacks([runnable_error1,runnable_error2])

# 调用可运行对象
# result = chain.stream("下面给你吃")
# result = chain.stream("我给你我的附属金卡")
# print("result=",result)
# print("type(result)=",type(result))
# # 迭代输出并打印
#
# # str1 = "123456" #字符串属于可迭代对象,也会逐个字符进行迭代,这样下面每个字符都会换行
# # for item in str1:
# #     print(item)
# for item in result:
#     print(item)
result = fun1("12")
for item in result:
    print(item)