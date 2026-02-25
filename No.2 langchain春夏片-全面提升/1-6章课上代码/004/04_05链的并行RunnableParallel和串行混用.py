# RunnableParallel
#parallel并行的意思
from langchain_core.runnables import RunnableLambda, RunnableParallel


def add(a,b):
    result = a + b
    print("add()=", result)
    return result
def sub(a,b):
    result = a - b
    print("sub()=", result)
    return result
runnable2 = RunnableLambda(lambda x: add(x[0],x[1]))
runnable3 = RunnableLambda(lambda x: sub(x[0],x[1]))
# runnable2.invoke((1,1))
# runnable3.invoke((10,1))
# chain =  RunnableParallel(run1 = runnable2, run2 = runnable3)#语法,用任意命名的参数kwargs的语法,可以把其他runnable对象放进来,用逗号隔开
# chain = RunnableParallel({"run3":runnable2,"run4":runnable3})#语法:参数改成字典,里面的value类型是要Runnable的子类型
# chain =  {"run3":runnable2,"run4":runnable3} #直接用字典包含,不行

# print(chain)
# print("type(chain)=",type(chain))
# dic = chain.model_dump_json()#RunnableLambda类型不能被model_dump_json()
# dic = chain.to_json()
# print("dic=",dic)
# print("type(dic)=",type(dic))
# result = chain.invoke((1,1))
# print("result=",result)
# print("type(result)=",type(result))

#
def makeTuple(a,b):

    result = (a,b)
    print("调用制造元组makeTuple,生成的元组是=",result)
    return result
# makeTuple(1,1)
runnable1 = RunnableLambda(lambda x: makeTuple(x[0],x[1]))
runnable1.invoke((1,1))

# chain = runnable1 |  RunnableParallel({"run3":runnable2,"run4":runnable3})  #RunnableSerializable 生成顺序执行的
chain = runnable1 |  {"run3":runnable2,"run4":runnable3} # 管道操作符|强制转换,字典转并行 放在链里面可以省略外面的RunnableParallel
result = chain.invoke((1,1))
print(result)
print(type(result))
print(result["run3"])
print(result["run4"])




