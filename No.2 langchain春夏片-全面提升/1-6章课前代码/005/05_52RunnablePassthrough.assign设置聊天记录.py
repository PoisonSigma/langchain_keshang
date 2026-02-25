from operator import itemgetter

from langchain_core.messages import trim_messages
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory

trimmer = trim_messages(strategy="last", max_tokens=2, token_counter=len)#保留6句话
chain1 = RunnablePassthrough.assign(chat_history=itemgetter("chat_history") | trimmer)
result1 = chain1.invoke({"input": "你好我叫肘肘","chat_history":["这个是聊天历史记录1","这个是聊天历史记录2","这个是聊天历史记录3"]})
print("result1=",result1)