from operator import itemgetter

from langchain_core.messages import trim_messages
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个有用的助手。尽你所能回答所有的问题.",),
        ("placeholder", "{chat_history}"),  # 这里面自己往里输入修剪后的聊天历史
        ("human", "{input}"),  # 这里是用户自己的每次的输入
    ]
)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
prompt_chain = (
        prompt
        | llm
)
historyObj = ChatMessageHistory()


def getHistory(session_id: str):
    return historyObj


print("type(demo_ephemeral_chat_history)=", type(historyObj))
chain_with_history = RunnableWithMessageHistory(
    prompt_chain,
    getHistory,
    input_messages_key="input",
    history_messages_key="chat_history",
)
# 注意,RunnableWithMessageHistory只是监听聊天历史
# result1 = chain_with_history.invoke({"input": "你好,我叫肘肘", "chat_history":historyObj},config={"configurable": {"session_id": "001"}})
# print("1.chain_with_history=", chain_with_history)
# print("result1=", result1)
# print("chat_history=", historyObj)
# result2 = chain_with_history.invoke({"input": "我的家乡是哈尔滨:", "chat_history":historyObj},config={"configurable": {"session_id": "001"}})
# print("2.chain_with_history=", chain_with_history)
# print("result2=", result2)
# print("chat_history=", historyObj)
# result3 = chain_with_history.invoke({"input": "我叫什么名字?", "chat_history":historyObj},config={"configurable": {"session_id": "001"}})
# print("3.chain_with_history=", chain_with_history)
# print("result3=", result3)
# print("chat_history=", historyObj)
# result4 = chain_with_history.invoke({"input": "我的家乡是哪里?", "chat_history":historyObj},config={"configurable": {"session_id": "001"}})
# print("4.chain_with_history=", chain_with_history)
# print("result4=", result4)
# print("chat_history=", historyObj)

trimmer = trim_messages(strategy="last", max_tokens=4, token_counter=len)  # 从后开始算,用系统的len取长度,就是只显示最后2条
def chain_history_fun(input:str):
    trim_history = trimmer.invoke(historyObj.messages)#historyObj保存的对象没有变,但是把他修剪可以
    historyObj.clear()
    historyObj.add_messages(trim_history)
    print("重新装填后的historyObj=", historyObj)
    print("trim_history=",trim_history)
    print("type(trim_history)=",type(trim_history))
    for i in range(len(trim_history)):
        print("聊天记录",i,"=",trim_history[i])
    result1 = chain_with_history.invoke({"input": input, "chat_history":trim_history},config={"configurable": {"session_id": "001"}})
    print("result1=",result1)
    print("chain_with_history=",chain_with_history)
    print("historyObj=",historyObj)


chain_history_fun("你好,我叫肘肘")
chain_history_fun("我的家乡是哈尔滨:")
chain_history_fun("我叫什么名字?")
chain_history_fun("我的家乡是哪里?")



