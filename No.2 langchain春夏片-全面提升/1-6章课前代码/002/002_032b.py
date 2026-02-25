import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

# 加载环境变量，确保你的 .env 文件中包含 OPENAI_API_KEY
load_dotenv("../assets/openai.env")
# print("当前目录:", os.getcwd())
print(os.getenv("OPENAI_API_BASE"))

# 创建 OpenAI 语言模型实例
llm = OpenAI(
    temperature=0.7,  # 控制生成文本的随机性，值越大越随机
    max_tokens=150    # 生成文本的最大长度
)

# 定义要生成文本的提示
prompt = "请描述一下美丽的日落景象。"

# 调用模型生成文本
response = llm.invoke(prompt)

# 打印生成的文本
print(response)