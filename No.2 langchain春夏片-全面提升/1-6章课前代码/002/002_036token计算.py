import os

import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.callbacks.manager import get_openai_callback #需要包含langchain社区包
msg = "你好"
load_dotenv("../assets/openai.env")
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=0.8)
with get_openai_callback() as cb:
    # get_openai_callback() 是上下文表达式，返回一个上下文管理器对象。
    # as cb 将该对象赋值给变量 cb，
    # 在代码块中可以使用 cb 来获取 Token 使用的统计信息。
    # 当代码块执行完毕，上下文管理器的 __exit__() 方法会被调用，完成相关的清理工作。
    res = llm.invoke(msg)
# total_tokens: int = 0
#     prompt_tokens: int = 0
#     prompt_tokens_cached: int = 0
#     completion_tokens: int = 0
    print(cb.prompt_tokens)
    print(cb.completion_tokens)
    print(cb.total_tokens)
print(res.content)
print("response_metadata=" , res.response_metadata)

