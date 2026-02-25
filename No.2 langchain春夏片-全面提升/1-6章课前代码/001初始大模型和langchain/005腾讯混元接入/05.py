import os
from openai import OpenAI

# 构造 client
client = OpenAI(
    # api_key=os.environ.get("HUNYUAN_API_KEY"), # 混元 APIKey
api_key="sk-ISnpn1p7Q8RkOf1pHWKZb8Z6jjMZ0yXTwnsnIONRUOFrPhxO",  # 这里填入你的实际api_key
    base_url="https://api.hunyuan.cloud.tencent.com/v1", # 混元 endpoint
)
# 自定义参数传参示例
completion = client.chat.completions.create(
    model="hunyuan-turbo",
    messages=[
        {
            "role": "user",
            "content": "你好",
        },
    ],
    extra_body={
        "enable_enhancement": True, # <- 自定义参数
    },
)
print(completion)
print(completion.choices[0].message.content)