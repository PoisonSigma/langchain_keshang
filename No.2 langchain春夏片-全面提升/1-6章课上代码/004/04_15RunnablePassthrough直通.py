#passthrough 穿过的意思
from itertools import chain
from xml.dom.minidom import Document

from langchain_core.runnables import RunnablePassthrough
# @chain
# def add(a):
#     print("add",a)


chain1 = RunnablePassthrough() #这个东西,用invoke传入什么,就输出什么
result = chain1.invoke(3)
print(result)
dic = {"docs":[1,2,3, ]}
print("type(dic)=",type(dic))
result = RunnablePassthrough().invoke({"docs":[1,2,3] ,"question":"我传入的文档中最大的数字是什么?"})
print(result) #RunnablePassthrough(),调用invoke 传入什么就 输出什么
# list1 = result["docs"]
# for doc in list1:
#     print(doc)
