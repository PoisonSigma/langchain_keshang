from langchain.agents.middleware import SummarizationMiddleware
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv



load_dotenv("openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
summarization_middleware = SummarizationMiddleware(llm,
                                     trigger=("tokens", 20),  # 触发总结的token数字
                                     # trigger=[("fraction", 0.5)],  # 触发条件,按分数算,需要在上面模型设置# profile={"max_input_tokens": 20} #为了下面使用分数
                                     keep=("messages", 2),  # 大模型总结保留之后的发送的提示词
                                     summary_prompt="你是个高冷的助手,最多只能说40tokens{messages}"
                                     # 注意,这里的占位符,必须是{messages}
                                     )
from langchain.agents import create_agent
agent = create_agent(llm,middleware=[
summarization_middleware
])
from langchain_core.messages import HumanMessage, AIMessage
messages = [
    HumanMessage(content="你好"),
    AIMessage(content="你好,我是deepseek"),
    HumanMessage(content="我的名字是肘肘,是动漫jojo的同人改编版,今年18岁,性别男,替身使者是:白金体验镇魂曲"),
    AIMessage(content="你好肘肘,很高兴认识你"),
HumanMessage(content="请问我刚才说了什么?"),
]
from ps_debug import PoisonDebug
debug_callback = PoisonDebug()
# debug_callback = PoisonDebug(debug=False, print_all=False)#不带断点
ai_msg = agent.invoke({"messages":messages},
                      {
                            "configurable": {"session_id": "001"},
                          "callbacks":[
                              debug_callback
                          ]}
                      )
for msg in ai_msg.get("messages"):
    print ("msg=",msg)

#总结后的框架模板以:Here is a summary of the conversation to date开头