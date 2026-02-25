

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda,chain

# fun1 = lambda x:x+1
#相当于 匿名函数(x):
#        return x+1 #这个是lambda表达式的返回值
# result = fun1(1)
# print(result)#返回值


# print(fun1)
# print(type(fun1))
# print(fun1(1))
@chain  #chain(add_one)
def add_one(a):
    result = a + 1
    print("add_one调用 result=",result)
    return result


print(add_one)
print(id(add_one))
print(add_one)
print(id(add_one))
print(add_one)
print(id(add_one))

@chain
def run1(_): #这里是不传参数,给个_占位
    print("run1")
print(run1)
@chain
def run2(a): #这里是不传参数,给个_占位
    print("run2 a=",a)

#管道操作符可以强制类型转换 函数类型为 RunnableLambda
chain1 =  add_one | (lambda x:x+1)| (lambda x:x+1) | { "run2":run2,"run1":run1 }  # 管道操作符,会强制转换函数类型为RunnableLamda
# print("type(chain1)=",type(chain1)) #管道操作符,返回RunnableSequence对象,
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

chain1.invoke(3)
# chain1 = ChatPromptTemplate.from_template("")
# dic1 = chain1.to_json()
# print("dic1=",dic1)
# import json
# jsonStr = json.dumps(dic1, ensure_ascii=False, indent=2) #错误RunnableLambda不让json序列化
