import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.prebuilt import create_react_agent

# 加载环境变量
load_dotenv("../openai.env")

# 初始化大模型
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8
)

# 定义工具
@tool("london_accent_speaker")
def london_accent_converter(text: str) -> str:
    """Convert text to London accent."""
    result = "张嘴一口地道的伦敦味 May I help you sir?" + text
    print(f"工具被执行: {result}")
    return result

print(f"工具名是: {london_accent_converter.name}")

# ====================== 关键修正：用 with 块获取真正的 checkpointer 实例 ======================
DB_URI = "postgresql://postgres:postgres@localhost:5442/postgres?sslmode=disable"

# 必须通过 with 块进入上下文，才能拿到可操作的 PostgresSaver 实例
with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    # 首次运行执行 setup() 创建表（新版需在 with 块内调用）
    checkpointer.setup()

    # 创建 agent
    agent = create_react_agent(
        llm=llm,
        tools=[london_accent_converter],
        system_prompt="你是个高冷的助手,只能说40字,多了就没钱坐2路汽车回家了",
    )

    # 绑定 checkpointer 和 thread_id
    agent = agent.with_config({
        "configurable": {
            "checkpointer": checkpointer,
            "thread_id": "3"
        }
    })

    # 1. 发起初始问题
    print("\n=== 初始问题回答 ===")
    first_result = agent.invoke({
        "messages": [HumanMessage(content="你好,我是东北土鳖,想要假装从伦敦回来的,一嘴伦敦腔,请问,说你好怎么说?")]
    })
    print("最终答案:", first_result["messages"][-1].content)

    # 2. 查询历史问题
    print("\n=== 历史问题查询 ===")
    history_result = agent.invoke({
        "messages": [HumanMessage(content="我刚才问了什么?")]
    })
    for msg in history_result.get("messages"):
        print(f"[{msg.type}]: {msg.content}")