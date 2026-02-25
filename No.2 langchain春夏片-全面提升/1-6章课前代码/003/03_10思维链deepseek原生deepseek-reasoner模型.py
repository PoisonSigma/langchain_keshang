#注意,下面是deepseek官网的例子
# ,把第一轮对话返回的思维链reasoning_content,这个是推理过程,我们打印显示出来给用户
#然后把第一轮返回的最终结果content ,当做第二轮对话的,其中一部分内容:
#角色改成{'role': 'assistant', 'content': content},
#再把第二轮的新问题变成{'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"})
#第二轮传过去真正的输入是 一段带着 assistant 以往回答的答案 和 user 新提出问题的 输入,组合成新的输入,就是新的上下文
from openai import OpenAI


client = OpenAI(api_key="sk-c7cedb71b580441089441795780ac272", base_url="https://api.deepseek.com")

# Round 1
messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages
)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print(response)
# reasoning_content 是 DeepSeek 的 deepseek-reasoner 模型特有的返回字段，
# 用于提供模型的推理过程（如思维链，Chain-of-Thought）。
# 例如，当用户提问“9.11 和 9.8 哪个更大？”时，
# reasoning_content 可能包含类似以下的逻辑：
reasoning_content = response.choices[0].message.reasoning_content
print("reasoning_content=",reasoning_content)
content = response.choices[0].message.content
print("content=",content)
# Round 2
messages.append({'role': 'assistant', 'content': content})
messages.append({'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"})
print("第2轮messages=",messages)
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages
)
print("第二轮")
print(response)
reasoning_content = response.choices[0].message.reasoning_content
print("reasoning_content=",reasoning_content)
content = response.choices[0].message.content
print("content=",content)
# client.chat.completions.create 方法的作用是向 DeepSeek 的 API 发送请求，以获取大语言模型（如 deepseek-reasoner）对输入问题的响应。它的核心功能是向云端的大模型服务提交对话内容（messages），并接收生成的文本回复。
#下面是完整输出结果,总共用了1000多tokens
#第一轮:prompt_cache_hit_tokens 缓存命中数 0
#第二轮:prompt_cache_hit_tokens=128, prompt_cache_miss_tokens=67
# 查看缓存命中情况,deepseek官网参考地址:https://api-docs.deepseek.com/zh-cn/guides/kv_cache
# 在 DeepSeek API 的返回中，我们在 usage 字段中增加了两个字段，来反映请求的缓存命中情况：
# prompt_cache_hit_tokens：本次请求的输入中，缓存命中的 tokens 数（0.1 元 / 百万 tokens）
# prompt_cache_miss_tokens：本次请求的输入中，缓存未命中的 tokens 数（1 元 / 百万 tokens）
# /Volumes/SN7501T/AiAgent笔记和代码/课前代码/.venv/bin/python /Volumes/SN7501T/AiAgent笔记和代码/课前代码/003/03_10思维链deepseek原生.py
# 铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(-->
# ChatCompletion(id='6401e6cd-d990-48d7-ae05-c64aef20d468', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='To determine whether 9.11 or 9.8 is greater, we start by comparing their decimal parts. \n\n1. Rewrite 9.8 as 9.80 to have the same number of decimal places as 9.11:\n   \\[\n   9.11 \\quad \\text{and} \\quad 9.80\n   \\]\n\n2. Compare the tenths place:\n   - The tenths digit of 9.11 is 1.\n   - The tenths digit of 9.80 is 8.\n   - Since 8 is greater than 1, 9.80 has a larger tenths value.\n\n3. Converting to fractions:\n   - 9.11 is \\(9 + \\frac{11}{100}\\)\n   - 9.8 is \\(9 + \\frac{80}{100}\\)\n   - Comparing \\(\\frac{11}{100}\\) and \\(\\frac{80}{100}\\), \\(\\frac{80}{100}\\) is larger.\n\n4. Subtracting the two numbers:\n   \\[\n   9.80 - 9.11 = 0.69\n   \\]\n   The positive result confirms 9.80 is greater.\n\n5. Using money analogy:\n   - $9.80 (9 dollars and 80 cents) is more than $9.11 (9 dollars and 11 cents).\n\nAll methods confirm that 9.8 is greater than 9.11.\n\n\\[\n\\boxed{9.8}\n\\]', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None, reasoning_content="Okay, so I need to figure out whether 9.11 is greater than 9.8 or if 9.8 is greater than 9.11. Hmm, let me start by writing both numbers down to compare them properly. \n\nFirst, I know that when comparing decimals, you start from the leftmost digit and move to the right. Both numbers have the same whole number part, which is 9. So the difference must be in the decimal parts. \n\nLet me break them down. The first number is 9.11. The decimal part here is 0.11. The second number is 9.8, which can also be written as 9.80 to make the decimal places equal. So if I rewrite them, it's 9.11 versus 9.80. \n\nNow, comparing the tenths place: in 9.11, the tenths digit is 1, and in 9.80, the tenths digit is 8. Since 8 is greater than 1, that means 9.80 has a larger tenths value. Therefore, 9.8 should be greater than 9.11. \n\nWait, but maybe I should double-check. Another way to compare them is to convert both decimals to fractions with the same denominator. Let's try that. \n\nFor 9.11, the decimal part is 11 hundredths, so that's 11/100. For 9.8, the decimal part is 8 tenths, which is equivalent to 80/100. So comparing 11/100 and 80/100, clearly 80/100 is larger. Therefore, 9.8 is greater than 9.11. \n\nAlternatively, I could subtract the two numbers to see which one is bigger. Let's do 9.8 minus 9.11. \n\n9.8 minus 9.11. Align the decimals:\n\n```\n 9.80\n-9.11\n------\n 0.69\n```\n\nSince the result is positive (0.69), that means 9.8 is larger than 9.11. \n\nBut just to make sure I haven't made any mistakes here. Let me think again. Sometimes when numbers have different decimal places, it's easy to get confused. For instance, 9.11 is 9 and 11 hundredths, while 9.8 is 9 and 8 tenths. Since 8 tenths is equal to 80 hundredths, comparing 80 hundredths and 11 hundredths, 80 is definitely more. So yes, 9.8 is greater. \n\nAnother approach: think of money. If these are amounts of money, $9.11 versus $9.80. Which is more? $9.80 is 9 dollars and 80 cents, while $9.11 is 9 dollars and 11 cents. 80 cents is more than 11 cents, so again, $9.80 is more. \n\nI guess all methods point to 9.8 being greater. Maybe my initial thought was right. I don't see any error in my calculations here. So the conclusion is that 9.8 is greater than 9.11.\n\n**Final Answer**\nThe greater number is \\boxed{9.8}."))], created=1742978958, model='deepseek-reasoner', object='chat.completion', service_tier=None, system_fingerprint='fp_5417b77867_prod0225', usage=CompletionUsage(completion_tokens=997, prompt_tokens=18, total_tokens=1015, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=None, reasoning_tokens=687, rejected_prediction_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cached_tokens=0), prompt_cache_hit_tokens=0, prompt_cache_miss_tokens=18))
# reasoning_content= Okay, so I need to figure out whether 9.11 is greater than 9.8 or if 9.8 is greater than 9.11. Hmm, let me start by writing both numbers down to compare them properly.
#
# First, I know that when comparing decimals, you start from the leftmost digit and move to the right. Both numbers have the same whole number part, which is 9. So the difference must be in the decimal parts.
#
# Let me break them down. The first number is 9.11. The decimal part here is 0.11. The second number is 9.8, which can also be written as 9.80 to make the decimal places equal. So if I rewrite them, it's 9.11 versus 9.80.
#
# Now, comparing the tenths place: in 9.11, the tenths digit is 1, and in 9.80, the tenths digit is 8. Since 8 is greater than 1, that means 9.80 has a larger tenths value. Therefore, 9.8 should be greater than 9.11.
#
# Wait, but maybe I should double-check. Another way to compare them is to convert both decimals to fractions with the same denominator. Let's try that.
#
# For 9.11, the decimal part is 11 hundredths, so that's 11/100. For 9.8, the decimal part is 8 tenths, which is equivalent to 80/100. So comparing 11/100 and 80/100, clearly 80/100 is larger. Therefore, 9.8 is greater than 9.11.
#
# Alternatively, I could subtract the two numbers to see which one is bigger. Let's do 9.8 minus 9.11.
#
# 9.8 minus 9.11. Align the decimals:
#
# ```
#  9.80
# -9.11
# ------
#  0.69
# ```
#
# Since the result is positive (0.69), that means 9.8 is larger than 9.11.
#
# But just to make sure I haven't made any mistakes here. Let me think again. Sometimes when numbers have different decimal places, it's easy to get confused. For instance, 9.11 is 9 and 11 hundredths, while 9.8 is 9 and 8 tenths. Since 8 tenths is equal to 80 hundredths, comparing 80 hundredths and 11 hundredths, 80 is definitely more. So yes, 9.8 is greater.
#
# Another approach: think of money. If these are amounts of money, $9.11 versus $9.80. Which is more? $9.80 is 9 dollars and 80 cents, while $9.11 is 9 dollars and 11 cents. 80 cents is more than 11 cents, so again, $9.80 is more.
#
# I guess all methods point to 9.8 being greater. Maybe my initial thought was right. I don't see any error in my calculations here. So the conclusion is that 9.8 is greater than 9.11.
#
# **Final Answer**
# The greater number is \boxed{9.8}.
# content= To determine whether 9.11 or 9.8 is greater, we start by comparing their decimal parts.
#
# 1. Rewrite 9.8 as 9.80 to have the same number of decimal places as 9.11:
#    \[
#    9.11 \quad \text{and} \quad 9.80
#    \]
#
# 2. Compare the tenths place:
#    - The tenths digit of 9.11 is 1.
#    - The tenths digit of 9.80 is 8.
#    - Since 8 is greater than 1, 9.80 has a larger tenths value.
#
# 3. Converting to fractions:
#    - 9.11 is \(9 + \frac{11}{100}\)
#    - 9.8 is \(9 + \frac{80}{100}\)
#    - Comparing \(\frac{11}{100}\) and \(\frac{80}{100}\), \(\frac{80}{100}\) is larger.
#
# 4. Subtracting the two numbers:
#    \[
#    9.80 - 9.11 = 0.69
#    \]
#    The positive result confirms 9.80 is greater.
#
# 5. Using money analogy:
#    - $9.80 (9 dollars and 80 cents) is more than $9.11 (9 dollars and 11 cents).
#
# All methods confirm that 9.8 is greater than 9.11.
#
# \[
# \boxed{9.8}
# \]
# 第2轮messages= [{'role': 'user', 'content': '9.11 and 9.8, which is greater?'}, {'role': 'assistant', 'content': 'To determine whether 9.11 or 9.8 is greater, we start by comparing their decimal parts. \n\n1. Rewrite 9.8 as 9.80 to have the same number of decimal places as 9.11:\n   \\[\n   9.11 \\quad \\text{and} \\quad 9.80\n   \\]\n\n2. Compare the tenths place:\n   - The tenths digit of 9.11 is 1.\n   - The tenths digit of 9.80 is 8.\n   - Since 8 is greater than 1, 9.80 has a larger tenths value.\n\n3. Converting to fractions:\n   - 9.11 is \\(9 + \\frac{11}{100}\\)\n   - 9.8 is \\(9 + \\frac{80}{100}\\)\n   - Comparing \\(\\frac{11}{100}\\) and \\(\\frac{80}{100}\\), \\(\\frac{80}{100}\\) is larger.\n\n4. Subtracting the two numbers:\n   \\[\n   9.80 - 9.11 = 0.69\n   \\]\n   The positive result confirms 9.80 is greater.\n\n5. Using money analogy:\n   - $9.80 (9 dollars and 80 cents) is more than $9.11 (9 dollars and 11 cents).\n\nAll methods confirm that 9.8 is greater than 9.11.\n\n\\[\n\\boxed{9.8}\n\\]'}, {'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"}]
# 第二轮
# reasoning_content= Okay, let's see. The user is asking how many times the letter 'R' appears in the word 'strawberry'. First, I need to make sure I spell the word correctly to check each letter. Let's break it down letter by letter.
#
# Starting with S-T-R-A-W-B-E-R-R-Y. Wait, let me write it out: S, T, R, A, W, B, E, R, R, Y. Let me count again. So the letters are:
#
# 1. S
# 2. T
# 3. R
# 4. A
# 5. W
# 6. B
# 7. E
# 8. R
# 9. R
# 10. Y
#
# So positions 3, 8, and 9 are R's. That's three R's. But wait, sometimes people might misspell the word. Let me confirm the correct spelling of 'strawberry'. Yes, it's S-T-R-A-W-B-E-R-R-Y. So after the B and E, there are two R's before the Y. So that's R at position 3, and then two R's at positions 8 and 9. So total three R's.
#
# But maybe the user made a typo? Let me double-check. If I type 'strawberry', the letters are S-T-R-A-W-B-E-R-R-Y. Yes, three R's. Alternatively, maybe the user is testing attention to detail. Let me count again. S (1), T (2), R (3), A (4), W (5), B (6), E (7), R (8), R (9), Y (10). Three R's. So the answer should be 3.
# content= The word "strawberry" is spelled as **S-T-R-A-W-B-E-R-R-Y**. Let's count the letter **R**:
#
# 1. **R** (3rd letter)
# 2. **R** (8th letter)
# 3. **R** (9th letter)
#
# **Total Rs**: 3
#
# \[
# \boxed{3}
# \]
#
# Process finished with exit code 0
