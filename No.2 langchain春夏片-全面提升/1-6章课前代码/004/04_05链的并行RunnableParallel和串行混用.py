# RunnableParallel
#parallel并行的意思
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnableSerializable


def add(a, b):
    result = a + b
    print("add",result)
    return result

def sub(a,b):
    result = a - b
    print("sub", result)
    return result
runnable1 = RunnableLambda(lambda x :add(x[0],x[1]))
runnable2 = RunnableLambda(lambda x :sub(x[0],x[1]))
# runnable1.invoke((1,1))#正常调用
# runnable2.invoke((2,1))
chain = RunnableParallel(run1 = runnable1, run2 = runnable2)#直接调用
# result = chain.invoke((1,1))
# print("result=",result) #返回结果是字典
# print("type(result)=",type(result))
# print(result["run1"])
# print(result["run2"])

chain = RunnableParallel({"run1":runnable1, "run2":runnable2}) #等价于上面
# result = chain.invoke((1,1))
#返回可运行对象的输出。
# print("result=",result) #这里返回结果是字典
# print("type(result)=",type(result))

#和管道操作符\ 组合使用,可以省略外面的RunnableParallel ,直接用字典包装
def makeTuple(a,b):#这个方法生成一个元组
    print("运行makeTuple")
    result = (a,b)
    print("result=",result)
    return result
# makeTuple(1,2)
runnable0 = RunnableLambda(lambda x :makeTuple(x[0],x[1]))
# runnable0.invoke((1,1))
#跟管道操作符组合,可以省略RunnableParallel
# chain = runnable0 | RunnableParallel({"run1":runnable1, "run2":runnable2}) #组合成了RunnableSequence
chain = runnable0 | {"run1":runnable1, "run2":runnable2} #组合成了RunnableSequence
# json = chain.model_dump_json()#RunnableLambda不能转这么转
# json = chain.to_json()
#
# print("json=",json)
#下面是打印结果,先执行first,再执行last
# chain= first=RunnableLambda(lambda x: makeTuple(x[0], x[1])) middle=[] last={
#   run1: RunnableLambda(lambda x: add(x[0], x[1])),
#   run2: RunnableLambda(lambda x: sub(x[0], x[1]))
# }
print("chain=",chain)
print("type(chain)",type(chain))
chain.invoke((1,1)) #先执行 第一个makeTuple 返回结果(1,1),再把他作为2个函数add和sub的参数运行2个函数



