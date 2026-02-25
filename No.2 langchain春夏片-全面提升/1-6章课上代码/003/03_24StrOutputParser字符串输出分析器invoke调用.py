import os

from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    stop = "好",
    model=os.getenv("MODEL_NAME"), temperature=0.8)
ai_msg = llm.invoke("你好")
print("ai_msg=",ai_msg)
# print("类型是=",type(ai_msg))
# print("res.content=",ai_msg.content)
#为了后面使用chain链
# text = StrOutputParser().invoke(ai_msg)#langchain的输出解析器,是可以调用invoke
# #所有langchain能调用invoke的都能组成chain
# print("text=",text)
text2 = StrOutputParser().parse(ai_msg)#langchain自带的解析器的parse没有处理content
print("text2=",text2)
