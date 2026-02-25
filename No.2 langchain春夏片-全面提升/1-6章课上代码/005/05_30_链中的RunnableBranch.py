#RunnableBranch
# from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain_classic.schema.runnable import RunnableBranch, RunnableLambda
#RunnableBranch分支结构,的判断条件是,如果顺序检查里面的判断条件,如果有一个为真,
# 就执行后面的Runnable,只执行第一次检查合格的

chain1 = RunnableLambda(lambda str: "第1欠er,别人睡觉,我hao他凳子腿"+str)
chain2 = RunnableLambda(lambda str: "第2欠er,咪咪睡觉,我给它扒拉醒"+str)
chain3 = RunnableLambda(lambda str: "第三欠儿,别人没起床,他起床跌军被,还有棱有角的,给人拍醒" + str)
chain_default = RunnableLambda(lambda str: "第3欠er,大黄睡觉,我拿烤肠蹭它鼻子" + str)

def fun1(str1):
    print("fun1开始判断")
    if len(str1) < 5:
        return True
    else:
        return False
def fun2(str1):
    print("fun2开始判断")
    return len(str1) < 10



final_chain = RunnableBranch(
    (fun1,chain1),#第一个分支,如果成立,就不往下判断
    (fun2,chain2),#第2个分支
    (lambda str:len(str)<15, chain3),
    # fun1
    chain_default #最后一个参数default,是默认值,前面都不符合要求执行,是要一个Runnable或者,callable or mapping
)
result = final_chain.invoke("12345678901234")
print("result=",result)