from langchain.agents.middleware import ModelFallbackMiddleware
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("openai.env")

llm1 = ChatDeepSeek(
    model="deepseek-chat",#这里直接读取字符串,不从配置文件读取,方面理解
api_key="asdfadsf",#故意写一个错误的
     temperature=0.8)
llm2 = ChatDeepSeek(
    model="deepseek-chat222asdfasdf",#这里直接读取字符串,不从配置文件读取,方面理解
     temperature=0.8)
llm3 = ChatDeepSeek(
    model="deepseek-chat",#这里直接读取字符串,不从配置文件读取,方面理解
     temperature=0.8)
fallback_middleware = ModelFallbackMiddleware(llm2, llm3)
from langchain.agents import create_agent
from langchain_core.globals import set_debug
set_debug(True)
agent = create_agent(llm1,middleware=[
fallback_middleware
])
from langchain_core.messages import HumanMessage
messages = [HumanMessage(content="hello")]
ai_msg = agent.invoke(
        {"messages": messages},
        config={
        }
    )

