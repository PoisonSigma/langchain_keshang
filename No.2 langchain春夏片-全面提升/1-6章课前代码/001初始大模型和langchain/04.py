# Please install OpenAI SDK first: `pip3 install openai`
"""
注意下面代码运行会报错402，因为deepseek接入没有充值
"""
from openai import OpenAI

client = OpenAI(api_key="sk-d3241b8682c948b385a2c049664edc75", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)