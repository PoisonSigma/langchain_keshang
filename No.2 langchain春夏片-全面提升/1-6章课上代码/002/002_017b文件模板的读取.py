import os

from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI
#load_prompt 读取模板,里面带文件路径
t1 = load_prompt("../assets/002_017.yaml")
print(t1)

p1 = t1.format(cartoon = "北斗神拳",name = "健次郎")
print(p1)
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(p1)
print(res.content)
# o ma e wa mou xin dei yi lv