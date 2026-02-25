from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是一个戒色禁欲指导ai专家,可以会打相关问题,但是要简短言简意赅"),
    MessagesPlaceholder(variable_name="GasSpeedSystem", optional=True),  # 注意,这里如果不写,那么也不会被报错,属于optional_variables
    MessagesPlaceholder(variable_name="GasSlowDownSystem"),
    # 注意,默认optional = False,这里下面format不写会报错,因为他属于input_variables
    ("placeholder", "{hava_girlfriend}"),  # 这种默认是可以不写的optional_variables=['GasSpeedSystem', 'hava_girlfriend']
    ("ai", "{answer}"),  # 这里是用户自己的输入的之前的回答
    ("human", "有女朋友能禁欲戒色成功吗?")
])
print("prompt=", prompt)
result = prompt.format(answer="禁欲戒色可以让人变年轻",
                       hava_girlfriend=[("user", "我有女朋友怎么戒色?")],
                       GasSpeedSystem=[
                           ("human", "禁欲戒色有哪些好处?")],
                       GasSlowDownSystem=[
                           HumanMessage(content="百日筑基是需要100天吗?")
                       ]
                       )
print(result)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
chain = prompt | llm | StrOutputParser()
ai_msg = chain.invoke(input=dict(
    answer="禁欲戒色可以让人变年轻",
    hava_girlfriend=[("user", "我有女朋友怎么戒色?")],
    GasSpeedSystem=[
        ("human", "禁欲戒色有哪些好处?")],
    GasSlowDownSystem=[
        HumanMessage(content="百日筑基是需要100天吗?")
    ]
)
)
print("ai_msg=", ai_msg)
