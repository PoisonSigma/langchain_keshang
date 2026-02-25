#fall_back 意思是 备用 ,后退,作用,如果发现错误,就是用 [] List列表中的元素
from langchain_core.runnables import RunnableLambda,chain
@chain
def normalFun(a:int):
    if a == 1:
        print("正常运行")
    else:
        raise ValueError("错误")
@chain
def errorFun1(_):
    raise ValueError("1也错了错误")
    print("发现错误回退处理1")
@chain
def errorFun2(_):
    print("发现错误回退处理2")
# chain = normalFun.with_fallbacks(errorFun)#报错应该传入[]List :Input should be an instance of Sequence [type=is_instance_of, input_value=RunnableLambda(errorFun), input_type=RunnableLambda]
chain = normalFun.with_fallbacks([errorFun1, errorFun2])
chain.invoke(0)



