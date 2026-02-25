from langchain.agents import create_agent
from langchain.tools import tool

import os

from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
#注意@tool() 括号里面的内容是工具描述,默认是函数名,但是括号里有内容就覆盖函数名
#@tool(""london_accent_converter"),注意工具名不能是中文,否则报错
@tool
def london_accent_converter(text: str):
    """说话的时候变成伦敦口音"""
    result = "此时传来一口地道的伦敦味:may I help you sir然后再说:" + text
    print("工具被调用")
    print(f"result={result}")
    return result#注意这个返回结果是给 大模型用的
print(london_accent_converter.name)#.name是工具的名称,表示工具用途
agent = create_agent(
    llm,
    tools=[london_accent_converter],
system_prompt="你是一个有用的代理"
)

ai_msg =  agent.invoke(({
    "messages":[HumanMessage(content="请把这句话变成伦敦口音:hello world")]
}))
print(f"执行结果{ai_msg}")
for item in ai_msg["messages"]:
    print(type(item),"\n",item)
last_msg = ai_msg["messages"][-1]
print("last_msg",last_msg)

# {'messages':
#      [HumanMessage(content='请把这句话变成伦敦口音:hello world', additional_kwargs={}, response_metadata={}, id='aafb2dfb-ba68-4fb1-8110-0bd988412589'),
#       AIMessage(content='我来帮您把这句话变成伦敦口音。', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 57, 'prompt_tokens': 316, 'total_tokens': 373, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 256}, 'prompt_cache_hit_tokens': 256, 'prompt_cache_miss_tokens': 60}, 'model_provider': 'deepseek', 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_eaab8d114b_prod0820_fp8_kvcache', 'id': '2b37b40a-00cf-455b-b7ec-8e1d6b066afe', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--019aeca0-19cf-79e3-90e3-4602b09321a1-0',
#                 tool_calls=[{'name': 'london_accent_converter', 'args': {'text': 'hello world'},
#                              'id': 'call_00_YH875VA4LE3mEBZn9GddnDyH', 'type': 'tool_call'}],
#                 usage_metadata={'input_tokens': 316, 'output_tokens': 57, 'total_tokens': 373, 'input_token_details': {'cache_read': 256},
#                                 'output_token_details': {}}),
#       ToolMessage(content='null', name='london_accent_converter', id='21fdd2bb-de45-457f-9a98-c62cda13e542',
#                   tool_call_id='call_00_YH875VA4LE3mEBZn9GddnDyH'),
#       AIMessage(content='看起来工具没有返回转换后的文本。让我再试一次，或者您可以告诉我您希望听到什么样的伦敦口音表达方式？比如：\n\n- "Ello, world!"（比较常见的伦敦腔问候）\n- "Alright, world?"（典型的伦敦问候方式）\n- "Hello there, world!"（带点伦敦腔调）\n\n您希望用哪种方式来表达呢？', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 76, 'prompt_tokens': 391, 'total_tokens': 467, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 384}, 'prompt_cache_hit_tokens': 384, 'prompt_cache_miss_tokens': 7}, 'model_provider': 'deepseek', 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_eaab8d114b_prod0820_fp8_kvcache', 'id': '592c4af6-0839-4ec6-9648-ba1ec057a6de', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--019aeca0-24d5-7a92-94dd-907cf8b47058-0', usage_metadata={'input_tokens': 391, 'output_tokens': 76, 'total_tokens': 467, 'input_token_details': {'cache_read': 384}, 'output_token_details': {}})]}