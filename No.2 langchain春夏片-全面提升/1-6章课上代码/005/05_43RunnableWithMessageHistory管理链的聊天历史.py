from langchain_core.messages import ChatMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
chain1 = ChatPromptTemplate.from_template("{name}")  | llm | StrOutputParser()
# result = chain1.invoke({"name":"你好"})
# print("result=",result)
history1 = ChatMessageHistory()
def history_fun(id:str):
    return history1
history_chain = RunnableWithMessageHistory( #可以监听 参数1的链的历史聊天记录,
    # 需要参数2里面返回的对象进行管理保存历史聊天记录
chain1,
lambda session_id: history1,
# history_fun,
#下面3行直接复制
input_messages_key = "name",#这个占位符,是RunnableWithMessageHistory的监听的链里面的占位符
history_messages_key = "chat_history2"
)
result2 = history_chain.invoke({"name":"你好"},{"configurable": {"session_id": "001"}})
print("result2=", result2)
print("history1=", history1)
# ({"input":"创建远程线程是什么意思?"},config={"configurable": {"session_id": "001"}})