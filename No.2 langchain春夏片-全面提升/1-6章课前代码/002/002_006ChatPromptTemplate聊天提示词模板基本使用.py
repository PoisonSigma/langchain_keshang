"""
PromptTemplate：适用于传统的基于文本生成的任务，在这种任务中，你只需要向语言模型提供一个单一的文本提示，然后模型根据这个提示生成相应的文本。例如，简单的文本摘要、文章生成、问题回答等场景，只需要将用户的需求以一个完整的文本形式呈现给模型。
ChatPromptTemplate：主要用于模拟聊天对话的场景，在这种场景中，对话通常由多个角色（如系统、用户、助手）的消息组成，并且消息之间存在一定的顺序和上下文关系。它更适合构建多轮对话、聊天机器人等应用，能够更好地处理复杂的交互逻辑。

"""
import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

#直译聊天提示模板

"""
常见且标准的角色类型  'human', 'user', 'ai', 'assistant', or 'system'.
"system"：系统消息通常用于为语言模型提供全局的指令或背景信息，它能引导模型以特定的方式进行回复。例如，在旅游顾问的例子中，("system", "你是一个专业的旅游顾问，擅长推荐旅游目的地。") 这一系统消息让模型明确自身的角色和任务。
"user" 或者 human ：用户消息代表与模型交互的用户输入内容。例如 ("user", "我想去 {destination} 旅游，你能给我一些建议吗？") 模拟了用户向模型提出问题的场景。
"assistant" 或者 ai：有时候也会用到 "assistant" 角色，它代表模型给出的回复消息。在一些更复杂的对话历史模拟或者提示构建中，会把之前模型的回复当作上下文信息加入，此时就会使用 "assistant" 角色。
ai" 和 "assistant" 被视为等价的消息角色类型。当你使用 ChatPromptTemplate.from_messages 方法构建聊天提示模板时，无论是使用 "ai" 还是 "assistant" 来代表模型的回复，langchain 都会以相同的方式处理这些消息。
"""
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ##系统消息模板，为模型提供一些初始指令
        # ("system", "你是一个反科技健身的视频up主,你的名字叫喜钟库尔曼"),
        # ("human", "我想写一篇搞笑的视频文案,写一个健美选手,他的名字是{name}"),
        # ("assistant",
        #  "文案开头以:类固醇星球传来喜讯,年仅多少岁的{name}移居蛋白质星球,每天7瓶蛋白粉尝尝咸淡,一天1万5千大卡摄入热量,深蹲时靠香草味的蛋白屁做氮气加速,组间歇去厕所肛门儿和马桶超级组,开头,后面写一些有意思的文案,要求100字以内"),
        ("system", "你是一个搞笑up主"),
        ("human", "我想写一篇搞笑的视频文案,内容是如何做一个程序员,他的名字叫{name}"),
        ("assistant",
         "文案开头以:代码圈传来喜讯,年仅20岁的程序员移居ai星球,每天靠动动脚趾就能完成工作,在家躺着赚钱,的文案,{count}字以内")
    ]
)
msg = chat_prompt_template.format(name="张三",count=80)
load_dotenv("../assets/openai.env")
print(os.getenv("OPENAI_API_BASE"))
#temperature=0.8 取值0-1之间的浮点数,0最精准,1发挥空间更大
llm = ChatOpenAI(model = os.getenv("MODEL_NAME"),temperature=0.8)
res = llm.invoke(msg)
print(res.content)

