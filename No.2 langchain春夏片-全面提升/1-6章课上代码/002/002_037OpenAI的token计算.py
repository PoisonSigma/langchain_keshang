import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.callbacks.manager import get_openai_callback
# grep -r "搜索字符串" "路径名"
"/Volumes/SN7501T/AiAgent笔记和代码/代码/课上代码/.venv/lib/python3.13/site-packages/langchain_community/"
"__enter__"
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.callbacks.manager import get_openai_callback
msg = "你好"
load_dotenv("../assets/openai.env")
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=0.8)
with get_openai_callback() as cb:
    res = llm.invoke(msg)
    print(cb.prompt_tokens) #提示词tokens
    print(cb.completion_tokens) #完成tokens
    print(cb.total_tokens) #总共tokens
    print("res.response_metadata=",res.response_metadata)
print(res.content)
print(cb.total_tokens)

