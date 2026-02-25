from langchain_core.runnables import chain,RunnableLambda
@chain
def add(dic1:dict):
    a = dic1["a"]
    b = dic1["b"]
    result = a + b
    print("add()=", result)
    return (result,1)#这里是为了返回元组,可以连续的invoke
# chain1 = RunnableLambda(add)
# chain1.invoke({"a":1,"b":2})
# print(type(chain1))
# print(type(add))
add.invoke({"a":1,"b":2})

