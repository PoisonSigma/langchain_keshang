from langchain_core.runnables import RunnableParallel, RunnablePassthrough
#passthrough穿过的意思
RunnablePassthrough
#RunnablePassthrough 的作用是原封不动地传递输入数据
runnable = RunnableParallel(
    passed=RunnablePassthrough(), #一般放在并联里面,内容是invoke传入的值
    modified=lambda x: x["num"] + 1,
)

result = runnable.invoke({"num": 1})
print(result)



result = RunnablePassthrough().invoke(3)#传入什么就输出什么
print(result)