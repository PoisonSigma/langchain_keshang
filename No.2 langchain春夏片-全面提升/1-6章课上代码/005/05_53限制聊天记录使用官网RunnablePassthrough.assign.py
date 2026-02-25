from operator import itemgetter

from langchain_core.messages import trim_messages
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
prompt =ChatPromptTemplate.from_messages(
[
        ("system", "你是一个全能的助手,什么都能回答,但是回答要简短,尽量在20个字以内,因为我喜欢简明扼要"),
        ("placeholder", "{bcd}"),  # 这里放历史聊天记录,如果有的话就放这里,这RunnableWithMessageHistory里是接收外层监听的RunnableWithMessageHistory传过来的聊天历史记录
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
trimer = trim_messages(
    max_tokens=4,
    token_counter=len,#用len是计算信息条数,不管信息多长,都算一条
    strategy="last",  # strategy="last",#last从后截取
)
#itemgetter("abc")获取上层RunnableWithMessageHistory输出的聊天记录对应的key 的value,然后生成一个新的key,再 用trimmer剪切,让聊天记录变短,再传给下层的提示词模板,
trimer_history_chain = RunnablePassthrough.assign(bcd = itemgetter("abc") | trimer) | prompt | llm | StrOutputParser()

historyObj = ChatMessageHistory()
final_chain = RunnableWithMessageHistory(
trimer_history_chain,
lambda x :historyObj,
input_messages_key = "input",#这个占位符,是RunnableWithMessageHistory的监听的链里面的占位符
history_messages_key = "abc" #这个是监听到的聊天记录,写入的key的名称,像下传递输出
)
def call_chain(shuoci:str):
    result = final_chain.invoke({"input": shuoci},
                              config={"configurable": {"session_id": "001"}})
    print("final_chain=",final_chain)
    print("result=",result)

call_chain("你好,我叫肘肘")
call_chain("你好,我的家乡是哈尔滨")
call_chain("我的名字是什么?")
call_chain("我的家乡是哪里?")
