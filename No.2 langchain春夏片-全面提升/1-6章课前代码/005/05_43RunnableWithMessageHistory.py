from langchain_core.messages import ChatMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
prmpt = ChatPromptTemplate.from_template("{name}")
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
chain1 = prmpt | llm | StrOutputParser()
get_history = ChatMessageHistory()


def get_history2(session_id):
    return ChatMessageHistory()
history1 = ChatMessageHistory()#类型是InMemoryChatMessageHistory
print("history1=",history1)
print("type(history1)=",type(history1))
def history1Fun(id:str):
    return history1

chain_with_message_history = RunnableWithMessageHistory(
    chain1,
    # lambda session_id: get_history,
    history1Fun,
    # 下面3行直接复制
    input_messages_key="name",
    history_messages_key="chat_history"
)
result = chain_with_message_history.invoke({"name": "你好"},
                                           {"configurable": {"session_id": "unused"}})

print("history1.messages=", history1.messages)
