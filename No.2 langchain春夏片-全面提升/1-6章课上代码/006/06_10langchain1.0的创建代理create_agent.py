import os

from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek

load_dotenv("../openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
#函数名也是工具名,但是@tool()装饰器,括号里面的字符串会覆盖工具名
# @tool
# @tool("伦敦东北人的发音")#错误,工具名不能是汉字
@tool("london_accent_speaker")
def london_accent_converter(text: str) -> str:
    """Convert text to London accent."""
    result = "张嘴一口地道的伦敦味 May I help you sir?" + text
    print(f"工具被执行{result}")
    return result #如果没有返回值,大模型就不用工具调用的结果,会自己想一出是一出,

print(f"工具名是:{london_accent_converter.name}")
agent = create_agent(llm,[london_accent_converter],
                     system_prompt="你是个高冷的助手,只能说40字,多了就没钱坐2路汽车回家了"
                     )
result = agent.invoke({"messages": [HumanMessage(content="你好,我是东北土鳖,想要假装从伦敦回来的,一嘴伦敦腔,请问,说你好怎么说?")]})
print("result=",result)
messages = result["messages"]
# for item in messages:
#     print(f"item={item}")
#     print(type(item))
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print("最终答案:",messages[-1].content)


# result["messages"]
# [HumanMessage(content='你好,我是东北土鳖,想要假装从伦敦回来的,一嘴伦敦腔,请问,说你好怎么说?', additional_kwargs={}, response_metadata={}, id='837abf0f-9abf-431f-a25c-5602cf970073'),
#  AIMessage(content='我可以用伦敦口音转换工具帮你把"你好"转换成伦敦腔的说法。让我来试试：', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 67, 'prompt_tokens': 324, 'total_tokens': 391, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 320}, 'prompt_cache_hit_tokens': 320, 'prompt_cache_miss_tokens': 4}, 'model_provider': 'deepseek', 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_eaab8d114b_prod0820_fp8_kvcache', 'id': 'd272cd53-ffc1-4246-a6c5-f6a895c53ee4', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--019aecd1-4d67-7c41-b742-a20475a2159e-0', tool_calls=[{'name': 'london_accent_converter', 'args': {'text': '你好'}, 'id': 'call_00_qGaqzdSq2UTNj7OCO8CYNlWl', 'type': 'tool_call'}], usage_metadata={'input_tokens': 324, 'output_tokens': 67, 'total_tokens': 391, 'input_token_details': {'cache_read': 320}, 'output_token_details': {}}),
#  ToolMessage(content='张嘴一口地道的伦敦味 May I help you sir?你好', name='london_accent_converter', id='03d47adb-1be6-4362-9281-59076ff2b900', tool_call_id='call_00_qGaqzdSq2UTNj7OCO8CYNlWl'),
#  AIMessage(content='根据转换结果，伦敦腔的"你好"可以说成："May I help you sir?"（我可以帮您吗，先生？）\n\n不过要注意，伦敦腔不仅仅是简单的翻译，而是一种特定的口音和表达方式。如果你想假装从伦敦回来，除了学会一些特定的表达外，还需要注意：\n\n1. 发音特点：伦敦腔（特别是Cockney口音）有一些独特的发音特点\n2. 用词习惯：比如用"mate"代替"friend"，"cheers"代替"thanks"等\n3. 语调：伦敦腔的语调比较特别\n\n你可以告诉我更多你想转换的句子，我可以帮你把它们变成伦敦腔的表达方式！', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 138, 'prompt_tokens': 421, 'total_tokens': 559, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 384}, 'prompt_cache_hit_tokens': 384, 'prompt_cache_miss_tokens': 37}, 'model_provider': 'deepseek', 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_eaab8d114b_prod0820_fp8_kvcache', 'id': 'e942a12d-523b-4ee9-8c2e-768aafcce433', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--019aecd1-5b7f-7600-8ba1-ffb46a57f743-0', usage_metadata={'input_tokens': 421, 'output_tokens': 138, 'total_tokens': 559, 'input_token_details': {'cache_read': 384}, 'output_token_details': {}})]

# {'messages': [HumanMessage(content='你好,我是东北土鳖,想要假装从伦敦回来的,一嘴伦敦腔,请问,说你好怎么说?', additional_kwargs={}, response_metadata={}, id='821320b4-2e53-46c3-995f-f203826c26af'), AIMessage(content='我可以用伦敦口音转换工具帮你把"你好"转换成伦敦腔的说法。让我来为你转换一下：', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 69, 'prompt_tokens': 324, 'total_tokens': 393, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 320}, 'prompt_cache_hit_tokens': 320, 'prompt_cache_miss_tokens': 4}, 'model_provider': 'deepseek', 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_eaab8d114b_prod0820_fp8_kvcache', 'id': '3a0d9226-677d-4ee7-a71c-b9ff51603e3a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--019aecd5-a847-7092-8a7c-1bb5618537ec-0', tool_calls=[{'name': 'london_accent_converter', 'args': {'text': '你好'}, 'id': 'call_00_OkYKixg4aD8sqPiF4SwXfTxR', 'type': 'tool_call'}], usage_metadata={'input_tokens': 324, 'output_tokens': 69, 'total_tokens': 393, 'input_token_details': {'cache_read': 320}, 'output_token_details': {}}), ToolMessage(content='null', name='london_accent_converter', id='293c07c4-9ab2-49c5-9004-6808eadbc601', tool_call_id='call_00_OkYKixg4aD8sqPiF4SwXfTxR'), AIMessage(content='看起来工具没有返回具体结果。不过我可以告诉你，在伦敦腔中，"你好"通常会说成：\n\n"Alright?" 或者 "Hello there, mate!"\n\n伦敦腔的特点包括：\n1. 喜欢用"mate"（伙计）称呼别人\n2. 经常用"innit"（是不是）结尾\n3. 发音比较懒散，比如"water"会发成"wa\'er"\n4. 有些独特的俚语，比如"cheers"可以表示谢谢\n\n如果你想假装从伦敦回来，可以说：\n- "Alright, mate?"（你好，伙计？）\n- "How\'s it going?"（最近怎么样？）\n- "Cheers!"（谢谢/再见）\n\n你想练习什么特定的句子吗？我可以帮你转换成伦敦腔的风格。', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 158, 'prompt_tokens': 411, 'total_tokens': 569, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 384}, 'prompt_cache_hit_tokens': 384, 'prompt_cache_miss_tokens': 27}, 'model_provider': 'deepseek', 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_eaab8d114b_prod0820_fp8_kvcache', 'id': '6b6d7c59-46f3-42ba-b4e5-0da7234f1ff1', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--019aecd5-b57c-7aa2-b029-6d04d41d91e2-0', usage_metadata={'input_tokens': 411, 'output_tokens': 158, 'total_tokens': 569, 'input_token_details': {'cache_read': 384}, 'output_token_details': {}})]}