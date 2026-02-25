from operator import itemgetter

from langchain_core.messages import trim_messages
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
trimmer = trim_messages(strategy="last", max_tokens=6, token_counter=len)#保留6句话
prompt =ChatPromptTemplate.from_messages(
[
        ("system", "你是一个全能的助手,什么都能回答,但是回答要简短,尽量在20个字以内,因为我喜欢简明扼要"),
        ("placeholder", "{chat_history}"),  # 这里放历史聊天记录,如果有的话就放这里
        ("human", "{input}"),  # 这里是最终的用户输入
    ]
)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
chain_with_trimming = (
    #这里的itemgetter 是读取字典的 chat_history2 字段,这个字段是从外面的调用链RunnableWithMessageHistory,产生的历史记录
    RunnablePassthrough.assign(chat_history=itemgetter("chat_history2") | trimmer)
    | prompt
    | llm
)





historyObj = ChatMessageHistory()
chain_with_trimmed_history = RunnableWithMessageHistory(
    chain_with_trimming,
    lambda session_id: historyObj,
    input_messages_key="input",
    history_messages_key="chat_history2",
)

def call_history(input:str):
    print("chain_with_trimmed_history=",chain_with_trimmed_history)
    print("historyObj=",historyObj)
    result1 = chain_with_trimmed_history.invoke({"input": input},
                          config={"configurable": {"session_id": "001"}})
    print(result1)
call_history("你好我叫肘肘")
call_history("我家乡是哈尔滨")
call_history("我叫什么")
call_history("我家乡是哪里?")


