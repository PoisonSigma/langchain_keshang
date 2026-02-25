import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI  # 注意,这个是langchain里面的OpenAI,跟openai包里面的OpenAI不是一个东西

msg = "你好"
load_dotenv("../assets/openai.env")
# print("当前目录:", os.getcwd())
print(os.getenv("OPENAI_API_BASE"))
# 使用 option+shift+e运行局部代码块的时候, python console的目录是根目录,不是当前文件所在目录
# 如果更改python console的当前目录使用命令os.chdir("完整路径") ,python console可以执行普通的python 代码,例如打等
# llm = ChatOpenAI(
#     model=os.getenv("MODEL_NAME")
# )
# res1= llm.invoke(msg)
# print(res1.content)

llm2 = OpenAI(
    # openai_api_base=os.getenv("OPENAI_API_BASE"),
    # openai_api_key=os.getenv("OPENAI_API_KEY"),
    # model_name=os.getenv("MODEL_NAME"),
    temperature=0,
    max_tokens = 256
    # max_retries=2,#生成时的最大重试次数
)
res2 = llm2(msg)
# print(res2.content)
