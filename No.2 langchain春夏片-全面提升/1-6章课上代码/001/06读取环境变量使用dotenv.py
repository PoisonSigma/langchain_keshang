import os
from dotenv import load_dotenv
#安装python-dotenv    .env文件, 通常在git当中放在忽略文件中
load_dotenv("../assets/openai.env")
#load_dotenv 是 python-dotenv 库中的一个函数，
# 它的主要作用是从 .env 文件中读取环境变量，
# 并将这些变量加载到当前 Python 程序的环境中。以下详细介绍其作用和使用场景：
#os os 库作为 Python 标准库的重要组成部分，为开发者提供了与操作系统交互的基础功能
api_key=os.environ.get("HUNYUAN_API_KEY")
name=os.getenv("NAME")
print(api_key)
print(name)

from openai import OpenAI

# 构造 client
client = OpenAI(
    api_key=os.environ.get("HUNYUAN_API_KEY"), # 混元 APIKey
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




