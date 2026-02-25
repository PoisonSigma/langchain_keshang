from operator import itemgetter

from langchain_core.messages import trim_messages
from langchain_core.runnables import RunnablePassthrough
# def add(x):
#     return {"name": x}
#RunnablePassthrough.assign 必须传入一个字典, ,并且把输出结果把原来输入的
result = RunnablePassthrough.assign(aka=lambda input: input['name'] + "屎山之王"  ).invoke({"name":"张三"})
print(result)
trimmer = trim_messages(
    max_tokens=30,
    token_counter=len,
    strategy="last",  # strategy="last",#last从后截取
)
result = RunnablePassthrough.assign(chat_history=lambda input: input['name'] + "屎山之王"  ).invoke({"name":"张三"})
print(result)


# itemgetter("name")( 字典) 是获取字典里面的key name
result = itemgetter("name")({"name":"张三"})
print(result)
#跟上面效果一样
result = RunnablePassthrough.assign(chat_history=lambda input:itemgetter("name")(input) + "屎山之王"   ).invoke({"name":"张三"})
print(result)