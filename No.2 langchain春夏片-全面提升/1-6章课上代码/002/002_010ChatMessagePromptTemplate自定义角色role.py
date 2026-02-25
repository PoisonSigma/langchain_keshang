"""
ChatMessagePromptTemplate 创建的角色：适用于需要标准化、高效回复的场景，如客服咨询、信息查询等。例如，将模型设定为 “旅游顾问”，可以快速为用户提供旅游景点、行程规划等方面的建议。
人类角色：在需要情感交流、创意协作和复杂决策的场景中具有不可替代的作用，如心理咨询、艺术创作等。
ChatMessagePromptTemplate里的角色时，主要是依据自身已有的训练数据和内部的语言理解、生成机制来进行操作。训练数据是大模型知识的主要来源，其中包含了各种各样的文本信息，涵盖不同领域、主题和语言表达方式等。当遇到ChatMessagePromptTemplate定义的角色时，模型会在这些已有的训练数据中寻找相关的模式
"""
import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
#下面例子,我们用自定义的角色吉良吉影跟ai对话,ai会把我们当成吉良吉影
#吉良吉影自我介绍:在某某百货公司上班,每天最晚8点回家，不抽烟，浅尝酒类，晚上11点睡，每天睡足8小时，睡前喝一杯温牛奶，做20分钟柔软操,一觉睡到天亮
#你在说什么啊?
#吉良吉影:你就是阻碍我睡眠的的烦恼
from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI

template1 = ChatMessagePromptTemplate.from_template(role="吉良吉影",template="每天工作到下午{t1}点就逃班，抽烟，去商场猛尝酒类,晚上11点开始熬夜，每天熬足{t2}小时，睡前喝7杯蛋白粉，做20分钟哑铃操，一觉睡到第二天下午{t3}点" )
hm1 = template1.format(t1=4, t2=8, t3=4)
print(hm1)
template2 = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是jojo里的角色:矢安宫重清"),
    HumanMessage(content="我每天工作到下午4点就逃班，抽烟，去商场猛尝酒类,晚上11点开始熬夜，每天熬足8小时，睡前喝7杯蛋白粉，做20分钟哑铃操，一觉睡到第二天下午4点"),
# hm1,
    AIMessage(content="你到底想说什么啊?"),
    # ChatMessagePromptTemplate.from_template(role="吉良吉影",template = "你听了我上面的自我介绍,就知道了我的秘密,我想说的是你知道我的替身使者叫什么名字吗?")
    # ChatMessagePromptTemplate.from_template(role="吉良吉影",template = "你听了我上面的自我介绍,就知道了我的秘密,我想说你是导致我失眠的人")
    HumanMessage(content="你听了我上面的自我介绍,就知道了我的秘密,我想说你是导致我失眠的人")
])
msg = template2.format()
print(msg)
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(msg)
print(res.content)
