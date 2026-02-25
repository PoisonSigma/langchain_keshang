
#https://console.cloud.tencent.com/hunyuan/api-key

import os
from openai import OpenAI

# 构造 client
client = OpenAI(
    # api_key=os.environ.get("HUNYUAN_API_KEY"), # 混元 APIKey
    api_key="这里同学填写自己的apikey",

    base_url="https://api.hunyuan.cloud.tencent.com/v1", # 混元 endpoint
)


# 自定义参数传参示例
response = client.chat.completions.create(
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
print(response)
print("手离>=======)====(===>")
print(response.choices[0].message.content)
