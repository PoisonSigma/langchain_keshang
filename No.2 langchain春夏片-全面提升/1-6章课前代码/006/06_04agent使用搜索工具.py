import os

from langchain.tools import BaseTool
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from typing import Optional
import requests
import json
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv("../assets/openai.env")



from langchain.agents import initialize_agent, AgentType, create_tool_calling_agent, AgentExecutor


# 初始化语言模型
import os
from langchain_deepseek import ChatDeepSeek
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
from langchain_core.tools import tool
# 创建工具实例
@tool
def web_search_tool(query: str):
    """网络搜索工具,当需要找最新信息的时候用这个工具"""
    print("调用本地的查询工具web_search_tool()")
    url = "https://api.langsearch.com/v1/web-search"
    from dotenv import load_dotenv
    load_dotenv("../assets/openai.env")
    payload = json.dumps({
        "query":query,  # 查询问题
        "freshness": "noLimit",
        "summary": True,
        "count": 1  # 这个结果不要太多:
    })
    headers = {
        'Authorization': os.getenv("LangSearchAPI"),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    # 解析JSON响应
    data = response.json()

    # 提取结果列表（注意观察响应结构）
    try:
        # 根据API返回的实际数据结构访问
        web_pages = data['data']['webPages']
        list1 = web_pages['value']

        print(f"找到 {len(list1)} 条结果：")
        result = ""
        for item in list1:
            result += "\n标题: " + str(item.get('name', ""))
            result += "\n链接: " + str(item.get('url', ""))
            result += "\n摘要: " + str(item.get('summary', ""))
            result += "\n发布时间: " + str(item.get('datePublished', ""))
            return result
    except KeyError as e:
        print("响应数据结构异常，缺少关键字段:", e)
        print("完整响应内容：")
        print(json.dumps(data, indent=2, ensure_ascii=False))

# rerank_tool = LangSearchRerankTool()# 文档重新排序工具
tools = [web_search_tool]


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "“你是一个有用的助手。不一定每次查询都使用工具——用户可能只是想聊天,回答问题言简意赅控制在20字以内",
        ),
        ("placeholder", "{messages}"),
        ("placeholder", "{agent_scratchpad}"),#scratchpad暂存器,#这个是下面的创建调用过工具的agent的可选输入值占位符
    ]
    )
#创建代理,并且传入工具,可以让大模型调用工具
agent = create_tool_calling_agent(llm, tools, prompt)
print("agent=", agent)
#创建代理执行器executor是执行器的意思
#verbose=True,使用详细模式运行 ,这个选择True会有一个绿色打印Entering new AgentExecutor chain...
#agent跟普通的langchain区别:
# agent多了决策能力和自动决定是否使用外部工具,但是普通langchain
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
print("agent_executor=", agent_executor)
from langchain_core.messages import HumanMessage

ai_msg = agent_executor.invoke({"messages":[HumanMessage(content="在网上查一下2025年5月17日哈尔滨天气预报")]})
print(ai_msg)