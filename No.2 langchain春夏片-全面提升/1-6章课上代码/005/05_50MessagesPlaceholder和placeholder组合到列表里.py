from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="你是一个运动专家"),
        MessagesPlaceholder(variable_name="human_input1"),  # 等价于:("placeholder", "{chat_history}")
         ("placeholder", "{answer}"),  # 这里放历史聊天记录,如果有的话就放这里
        ("human", "{human_final_input}"),  # 这里是最终的用户输入
    ]
)
print("prompt=",prompt)
result = prompt.format(human_final_input="我不装了,我就想变帅,其他什么都不要",
                       human_input1=[
                           HumanMessage(content="我想刷脂")
                       ],
answer=[]
                       )
# print(result)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
chain = prompt | llm | StrOutputParser()
ai_msg = chain.invoke(dict(human_final_input="我不装了,我就想变帅,其他什么都不要",
                       human_input1=[
                           HumanMessage(content="我想刷脂")
                       ],
answer=[]
                      ))
print("ai_msg",ai_msg)
# dic1 = dict(name = "张三")
# print(dic1)

