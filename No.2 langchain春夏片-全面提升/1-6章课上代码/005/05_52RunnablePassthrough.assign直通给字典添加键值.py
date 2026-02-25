from operator import itemgetter

from langchain_core.messages import trim_messages
from langchain_core.runnables import RunnablePassthrough
def isHaveSpeedUpSystem_fun(input:str):
    return "abc"
chain1 = RunnablePassthrough.assign(isHaveSpeedUpSystem=isHaveSpeedUpSystem_fun)
#RunnablePassthrough.assign必须传入字典
result = chain1.invoke({"name":"张木枝"})
#把之前传入的一个键值对,保留,直通,然后新生成一个键值对,
# 但是是用函数返回的值作为value
print(result)

chain1 = RunnablePassthrough.assign(chat_history=lambda x: x["name"])
result = chain1.invoke({"name":"张木枝"})
#把之前传入的一个键值对,保留,直通,然后新生成一个键值对,
# 但是是用函数返回的值作为value
print(result)

dic1 = {"name":"张木枝"}
result = itemgetter("name")(dic1)
print(result)
result = itemgetter("name")( {"name":"张木枝"})
print(result)
fun1 = itemgetter("name")
print(fun1)
print(type(fun1))
print(fun1(dic1))
chain1 = RunnablePassthrough.assign(aka=itemgetter("name")) #直接给函数名,就省略传入参数了
result = chain1.invoke({"name":"张木枝"})
print(result)

chain1 = RunnablePassthrough.assign(aka=lambda x: itemgetter("name")(x)) #这个是完整的函数调用
result = chain1.invoke({"name":"张木枝"})
print(result)


trimer = trim_messages(
    max_tokens=2,
    token_counter=len,#用len是计算信息条数,不管信息多长,都算一条
    strategy="last",  # strategy="last",#last从后截取
)
chain1 = RunnablePassthrough.assign(aka=itemgetter("name") | trimer) #这个是完整的函数调用
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
# result = chain1.invoke({"name":"123456789"}) #字符串可以被迭代,按照字符迭代
# print(result)
result = chain1.invoke({"name":["11111","2222","3333"]}) #字符串可以被迭代,按照字符迭代
print(result)