from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain,RunnableLambda
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    stop = "好",
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
@chain
def chain1(dic1:dict):
    text1 = dic1["text1"]
    text2 = dic1["text2"]
    text3 = text1 + text2
    print(text3)
    prompt = ChatPromptTemplate.from_template("{str1}").partial(str1 = text3)
    ai_msg = (prompt | llm | StrOutputParser()).invoke({})
    return ai_msg

outPut =  chain1.invoke({"text1":"你","text2":"好"})
print(outPut)
