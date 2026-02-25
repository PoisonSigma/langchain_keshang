# agent跟普通的langchain区别:
# agent多了决策能力和自动决定是否使用外部工具,但是普通langchain
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
import os
import requests
import json


@tool
def web_search_tool(query: str):
    """网络搜索工具,当需要找最新信息的时候用这个工具"""
    # 区别在于url不同,一个是rerank,翻译过来叫重新排序,一个叫web-search,是网络搜索
    print("开始调用本地工具web_search_tool()")
    url = "https://api.langsearch.com/v1/web-search"  # 网络查询的接口地址
    from dotenv import load_dotenv
    load_dotenv("../assets/openai.env")
    payload = json.dumps({  # 给接口传入的数据
        "query": query,  # 查询问题
        "freshness": "noLimit",
        "summary": True,  # 总结
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
            print("item", item)
            result += "\n标题: " + item.get('name', "")
            result += "\n链接: " + item.get('url', "")
            result += "\n摘要: " + item.get('summary', "")
            result += "\n发布时间: " + item.get('datePublished', "")
        print("result=", result)
        return result
    except KeyError as e:
        print("响应数据结构异常，缺少关键字段:", e)
        print("完整响应内容：")
        print(json.dumps(data, indent=2, ensure_ascii=False))  # 按缩进打印json


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "“你是一个有用的助手。不一定每次查询都使用工具——用户可能只是想聊天,回答问题言简意赅控制在20字以内",
        ),
        ("placeholder", "{chat_history}"),
        ("placeholder", "{messages2}"),

        ("placeholder", "{agent_scratchpad}"),  # scratchpad暂存器,#这个是下面的创建调用过工具的agent的可选输入值占位符
    ]
)

tools = [web_search_tool]
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
# 创建代理,并且传入工具,可以让大模型调用工具
agent = create_tool_calling_agent(llm, tools, prompt)
# verbose=True,使用详细模式运行 ,这个选择True会有一个绿色打印Entering new AgentExecutor chain...
# 创建代理执行器executor是执行器的意思
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = "你好,我是秦始皇,告诉我哈尔滨市2025年5月16日天气预报"
# query = "你好,我是空条承太郎,我从动漫世界来到现实世界,现在继续1个亿,就能打败jojo第六步里的神父,告诉我如何赚到1个亿"
# output
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

historyObj = ChatMessageHistory()

agent_executor_history = RunnableWithMessageHistory(
    agent_executor,
    lambda session_id: historyObj,
    input_messages_key="messages2",
    history_messages_key="chat_history",
    output_messages_key= "output", #如果打开注释,里面的output不能写错,因为真的要用
)


def call_agent(input: str):
    ai_msg = agent_executor_history.invoke({"messages2": [HumanMessage(content=input),]},
                                           {"configurable": {"session_id": "001"}})

    print("agent_executor_history=", agent_executor_history)
    print("ai_msg=", ai_msg)
    print("historyObj=", historyObj)


call_agent("爱卿平身,我是秦始皇")
call_agent("我是谁?")
call_agent("我叫什么名字?")
