# 而是一个独立的人工智能应用开发框架。
# 它通过封装和集成多种大语言模型（LLM）的 API（包括 OpenAI、Anthropic、Cohere 等），
# 为开发者提供统一的接口来构建复杂的 AI 应用。

#在 langchain 库中，OpenAI 和 ChatOpenAI 都是用于与 OpenAI 模型进行交互的类，但它们在使用场景、输入输出格式、适用模型等方面存在明显区别，以下是详细介绍：
#langchain的 OpenAI输入字符串,返回字符串,但是ChatOpenAI,是可以对话形式,输出一堆臭氧层子,返回一堆臭氧层子,建议使用

# OpenAI：主要用于传统的文本生成任务，例如撰写文章、生成故事、描述场景等，适用于只需单向文本生成的简单场景。
# ChatOpenAI：专门为对话式交互设计，适合构建聊天机器人、问答系统等需要多轮对话的场景，能更好地处理上下文信息。
import os

from dotenv import load_dotenv
from openai import OpenAI as OpenAI_old #这个是OpenAI的库,起别名成OpenAI_old
#注意,下面的OpenAI_old是openai 包里面的,这个要使用,
load_dotenv("../assets/openai.env")
print("当前目录:", os.getcwd())
print(os.getenv("OPENAI_API_BASE"))
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_API_BASE")

class PsBigChain(OpenAI_old):
    def __init__(self):
            #self.llm 在init方法里面self.变量名是
            #使用 self.变量名 赋值时，就会在实例对象上创建一个新的属性，也就是成员变量。
        self.llm = OpenAI_old(
            api_key=api_key,
            base_url=base_url
        )
    def invoke(self,msg:str)->str:
        #这里是别的方法使用对象的成员变量,就用self.成员变量名
        completion = self.llm.chat.completions.create(
            model="hunyuan-turbo",
            messages=[
                {
                    # 常见且标准的角色类型  'human', 'user', 'ai', 'assistant', or 'system'.
                    "role": "user",
                    "content": msg,
                },
            ],
            #OpenAI 官方 API 的标准参数
            # extra_body={
            #     "enable_enhancement": True,  # <- 自定义参数
            # },
        )
        content = completion.choices[0].message.content
        print("这是阿祖的vip专享invoke,必须2楼雅座请")
        return content
llm = PsBigChain()
res = llm.invoke("你好")
print(res)