# import ps_chain.chat_models
# from ps_chain import add

#直接用import会所有包下的内容全导入，调用里面的方法要加包名前缀.
import ps_chain
result:int = ps_chain.add(100, 4);
print(result)

def add(a, b):
    return a + b

result = add(3, 5)
print(result)

