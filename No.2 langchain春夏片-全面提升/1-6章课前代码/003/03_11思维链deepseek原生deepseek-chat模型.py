from openai import OpenAI


client = OpenAI(api_key="sk-c7cedb71b580441089441795780ac272", base_url="https://api.deepseek.com")

# Round 1
messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
response = client.chat.completions.create(
    model="deepseek-chat",#这里换了便宜的chat模型
    messages=messages
)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print(response)
#chat模型没有reasoning_content,因为这个是推理字段,只有reasoner 模型有推理过程
# reasoning_content = response.choices[0].message.reasoning_content
# print("reasoning_content=",reasoning_content)
print("response=",response)
content = response.choices[0].message.content
print("content=",content)
# Round 2
messages.append({'role': 'assistant', 'content': content})
messages.append({'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"})
print("第2轮messages=",messages)
response = client.chat.completions.create(
    model="deepseek-chat",#这里换了便宜的chat模型
    messages=messages
)
print("第二轮")
# reasoning_content = response.choices[0].message.reasoning_content
# print("reasoning_content=",reasoning_content)
print("response=",response)
content = response.choices[0].message.content
print("content=",content)
#下面是运行结果,可以看到chat模型没有思维链,消耗token 只有 total_tokens=384
# / Volumes / SN7501T / AiAgent笔记和代码 / 课前代码 /.venv / bin / python / Volumes / SN7501T / AiAgent笔记和代码 / 课前代码 / 003 / 03_11
# 思维链deepseek原生deepseek - chat模型.py
# 铭刻: 义父追魂戟, 把离手越进义父离你越远 > ---红字增幅 + 26 - ---------)三(-->
# ChatCompletion(id='bb3284bb-5c19-4c94-9078-a7dc60ffcda1', choices=[Choice(finish_reason='stop', index=0, logprobs=None,
#                                                                           message=ChatCompletionMessage(
#                                                                               content="To determine which number is greater between **9.11** and **9.8**, let's compare them step by step.\n\n### Step 1: Compare the Whole Number Part\nBoth numbers have the same whole number part:\n- **9.11** has **9**\n- **9.8** has **9**\n\nSince the whole numbers are equal, we proceed to compare the decimal parts.\n\n### Step 2: Compare the Tenths Place\n- **9.11** has **1** in the tenths place.\n- **9.8** has **8** in the tenths place.\n\n**8** is greater than **1**, so **9.8** is greater than **9.11**.\n\n### Final Answer\n\\[\n\\boxed{9.8}\n\\]",
#                                                                               refusal=None, role='assistant',
#                                                                               audio=None, function_call=None,
#                                                                               tool_calls=None))], created=1742981810,
#                model='deepseek-chat', object='chat.completion', service_tier=None,
#                system_fingerprint='fp_3d5141a69a_prod0225',
#                usage=CompletionUsage(completion_tokens=162, prompt_tokens=16, total_tokens=178,
#                                      completion_tokens_details=None,
#                                      prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cached_tokens=0),
#                                      prompt_cache_hit_tokens=0, prompt_cache_miss_tokens=16))
# response = ChatCompletion(id='bb3284bb-5c19-4c94-9078-a7dc60ffcda1', choices=[
#     Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(
#         content="To determine which number is greater between **9.11** and **9.8**, let's compare them step by step.\n\n### Step 1: Compare the Whole Number Part\nBoth numbers have the same whole number part:\n- **9.11** has **9**\n- **9.8** has **9**\n\nSince the whole numbers are equal, we proceed to compare the decimal parts.\n\n### Step 2: Compare the Tenths Place\n- **9.11** has **1** in the tenths place.\n- **9.8** has **8** in the tenths place.\n\n**8** is greater than **1**, so **9.8** is greater than **9.11**.\n\n### Final Answer\n\\[\n\\boxed{9.8}\n\\]",
#         refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1742981810,
#                           model='deepseek-chat', object='chat.completion', service_tier=None,
#                           system_fingerprint='fp_3d5141a69a_prod0225',
#                           usage=CompletionUsage(completion_tokens=162, prompt_tokens=16, total_tokens=178,
#                                                 completion_tokens_details=None,
#                                                 prompt_tokens_details=PromptTokensDetails(audio_tokens=None,
#                                                                                           cached_tokens=0),
#                                                 prompt_cache_hit_tokens=0, prompt_cache_miss_tokens=16))
# content = To
# determine
# which
# number is greater
# between ** 9.11 ** and ** 9.8 **, let
# 's compare them step by step.
#
# ### Step 1: Compare the Whole Number Part
# Both
# numbers
# have
# the
# same
# whole
# number
# part:
# - ** 9.11 ** has ** 9 **
# - ** 9.8 ** has ** 9 **
#
# Since
# the
# whole
# numbers
# are
# equal, we
# proceed
# to
# compare
# the
# decimal
# parts.
#
# ### Step 2: Compare the Tenths Place
# - ** 9.11 ** has ** 1 ** in the
# tenths
# place.
# - ** 9.8 ** has ** 8 ** in the
# tenths
# place.
#
# ** 8 ** is greater
# than ** 1 **, so ** 9.8 ** is greater
# than ** 9.11 **.
#
# ### Final Answer
# \[
# \boxed
# {9.8}
# \]
# 第2轮messages = [{'role': 'user', 'content': '9.11 and 9.8, which is greater?'}, {'role': 'assistant',
#                                                                                   'content': "To determine which number is greater between **9.11** and **9.8**, let's compare them step by step.\n\n### Step 1: Compare the Whole Number Part\nBoth numbers have the same whole number part:\n- **9.11** has **9**\n- **9.8** has **9**\n\nSince the whole numbers are equal, we proceed to compare the decimal parts.\n\n### Step 2: Compare the Tenths Place\n- **9.11** has **1** in the tenths place.\n- **9.8** has **8** in the tenths place.\n\n**8** is greater than **1**, so **9.8** is greater than **9.11**.\n\n### Final Answer\n\\[\n\\boxed{9.8}\n\\]"},
#                  {'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"}]
# 第二轮
# response = ChatCompletion(id='428f270a-2e37-4352-9ed7-370f5ff5f3d9', choices=[
#     Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(
#         content='To determine how many times the letter **R** appears in the word **"strawberry"**, let\'s write out the word and count each occurrence of **R**.\n\n### Step-by-Step Solution:\n\n1. **Write out the word:**\n   \n   ```\n   S T R A W B E R R Y\n   ```\n\n2. **Identify each letter and count the Rs:**\n   \n   - **S**  \n   - **T**  \n   - **R** (1)  \n   - **A**  \n   - **W**  \n   - **B**  \n   - **E**  \n   - **R** (2)  \n   - **R** (3)  \n   - **Y**  \n\n3. **Total Rs:**\n   \n   There are **3** instances of the letter **R** in "strawberry."\n\n### Final Answer:\n\\[\n\\boxed{3}\n\\]',
#         refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1742981821,
#                           model='deepseek-chat', object='chat.completion', service_tier=None,
#                           system_fingerprint='fp_3d5141a69a_prod0225',
#                           usage=CompletionUsage(completion_tokens=189, prompt_tokens=195, total_tokens=384,
#                                                 completion_tokens_details=None,
#                                                 prompt_tokens_details=PromptTokensDetails(audio_tokens=None,
#                                                                                           cached_tokens=128),
#                                                 prompt_cache_hit_tokens=128, prompt_cache_miss_tokens=67))
# content = To
# determine
# how
# many
# times
# the
# letter ** R ** appears in the
# word ** "strawberry" **, let
# 's write out the word and count each occurrence of **R**.
#
# ### Step-by-Step Solution:
#
# 1. ** Write
# out
# the
# word: **
#
# ```
# S
# T
# R
# A
# W
# B
# E
# R
# R
# Y
# ```
#
# 2. ** Identify
# each
# letter and count
# the
# Rs: **
#
# - ** S **
# - ** T **
# - ** R ** (1)
# - ** A **
# - ** W **
# - ** B **
# - ** E **
# - ** R ** (2)
# - ** R ** (3)
# - ** Y **
#
# 3. ** Total
# Rs: **
#
# There
# are ** 3 ** instances
# of
# the
# letter ** R ** in "strawberry."
#
# ### Final Answer:
# \[
# \boxed
# {3}
# \]
#
# Process
# finished
# with exit code 0
