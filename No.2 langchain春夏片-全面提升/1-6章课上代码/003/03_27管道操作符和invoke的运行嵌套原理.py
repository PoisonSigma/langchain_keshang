#LangChain表达式 LangChain表达式 (LCEL)
#一般顺序, 提示词 | llm | 解析器
# 前一个可运行对象的 .invoke() 调用的输出作为输入传递给下一个可运行对象。
from langchain_classic.chains.llm import LLMChain
from langchain_core.output_parsers import StrOutputParser
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
prompt = ChatPromptTemplate.from_template(
    "你好,我是{city}{name}"
)
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    stop="好",
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
#Serializable 可串行化的
#按顺序,做个提示词+ llm的链
msg = prompt.invoke({"city":"广东佛山","name":"吴彦祖"})
print("msg",msg)
# chain = prompt | llm
# chain.invoke({})

ai_msg = llm.invoke(prompt.invoke({"city":"广东佛山","name":"吴彦祖"}))
#上面的嵌套,相当于 # ( prompt | llm ) .invoke
# print("ai_msg",ai_msg)
parser = StrOutputParser()
# text = parser.invoke(ai_msg)
# print("text",text)
# text = parser.invoke(llm.invoke(prompt.invoke({"city": "广东佛山", "name": "吴彦祖"})))
# AKA shit montain king
chain = prompt | llm | parser
text = chain.invoke({"city": "广东佛山", "name": "吴彦祖"})#实际这里就是调用了3次invoke
#所有能调用invoke的方法,最终都可以在这个表达式里面一起调用invoke
print("text",text)

