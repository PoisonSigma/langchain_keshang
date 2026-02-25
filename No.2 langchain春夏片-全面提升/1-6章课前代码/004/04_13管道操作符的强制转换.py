

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.runnables import chain

fun1 = (lambda x:x+1)
print(fun1)
print(type(fun1))
fun1 (3)

@chain
def add_one(a):
    return a+1
chain1 = add_one | (lambda x:x+1) | (lambda x:x+1)
# result = chain1.invoke(3)
# print(result)

# chain2 =  (lambda x:x+2)  | (lambda x:x+1) #这样不行,至少有一个Runnable对象
# chain2.invoke(3)
# def run1():#报错:没有参数,但是chain函数要求入参类型是input有一个参数   Callable[[Input], Output],
@chain
def run1(a):   # 报错:没有参数,但是chain函数要求入参类型是input有一个参数   Callable[[Input], Output],

    print("run1 a=",a)
    return a+1
@chain
def run2(a:int):
    print("run2 a=",a)
    return a + 1
chain3 = add_one |  (lambda x:x+2)  | (lambda x:x+1) | {"run1":run1,"run2":run2}  #这样不行,至少有一个Runnable对象
chain3.invoke(3)