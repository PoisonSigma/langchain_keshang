from langchain_core.prompts import ChatPromptTemplate

# Adapted from https://smith.langchain.com/hub/jacob/tool-calling-agent
#官网使用的搜索工具是:TavilySearchResults ,这个是帮助在网络上搜索实时信息的,需要注册和付费,本课程不使用
#改成国内的:免费工具
from langchain_community.tools.tavily_search import TavilySearchResults
tools = [TavilySearchResults(max_results=1)]
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "“你是一个有用的助手。你可能不需要为每个查询都使用工具——用户可能只是想聊天,回答问题言简意赅控制在20字以内",
        ),
        ("placeholder", "{messages}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
    )
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
from langchain.agents import AgentExecutor, create_tool_calling_agent

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

from langchain_core.messages import HumanMessage

agent_executor.invoke({"messages": [HumanMessage(content="你好我叫肘肘")]})