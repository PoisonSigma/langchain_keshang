

# StrOutputParser可以大幅简化从LangChain中提取文本
# 假设有一个被绑定了工具的LLM
# 定义LLM使用claude
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    stop = "好",#出现好,就停止,只返回你
    model=os.getenv("MODEL_NAME"), temperature=0.8)

from langchain_core.output_parsers import StrOutputParser
#把字符串输出分析器 假如到链
parser = StrOutputParser()
chain = llm | parser
json = chain.model_dump_json()
print(json)
print("chain=",chain)
# 调用，可以很方便的取值
response = chain.invoke("你好")
print("response=",response) #这里不需要再用response.content

