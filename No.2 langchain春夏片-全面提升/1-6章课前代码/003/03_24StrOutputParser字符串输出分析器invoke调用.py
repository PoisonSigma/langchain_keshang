
# 定义LLM使用claude
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    stop = "好",#出现好,就停止,只返回你
    model=os.getenv("MODEL_NAME"), temperature=0.8)

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

# 调用，可以很方便的取值
response = llm.invoke("你好")
print("response=",response)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
#invoke()方法传入结果,获取content
result = parser.invoke(response)#直接使用分析器获取结果content
print("result=",result) #
result2 = parser.parse(response)#注意,langchain的分析器使用parse不能进行解析
print("result2=",result2) #

