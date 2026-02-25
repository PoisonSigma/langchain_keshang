from langchain_community.vectorstores import FAISS
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_huggingface import HuggingFaceEmbeddings
# HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
import os
# 设置环境变量，禁用 tokenizers 并行处理
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
# 创建 FAISS 向量数据库 ,
#from_texts()从原始文档构造FAISS包装器。
vectorstore = FAISS.from_texts(
    ["肘肘深蹲时候使用蛋气反重力系统",
     "肘肘锻炼肩膀中枢的时候使用重力对抗系统增加难度",
     "肘肘吃鸡蛋的时候用臀大肌夹碎鸡蛋"
     ],
    embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2"),
)
#这里面retriever的意义是,传递给大模型向量文档,让大模型参考回答问题的答案,这里传过去3个
retriever = vectorstore.as_retriever()#通过向量数据库创建检索器VectorStoreRetriever
print("retriever=",retriever)
result1 = retriever.invoke("肘肘深蹲时候用的什么系统?")
print("result1=",result1)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

prompt = ChatPromptTemplate.from_template(
"""请根据以下语境回答问题:
{context}
问题: {question}
"""
)
result1 = prompt.invoke({"context":"文档1,文档2","question":"我要回家干什么?"})
print("result1=",result1)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
runnableP =  RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
reusult2 = runnableP.invoke("肘肘深蹲时候用的什么系统?")
print("reusult2=",reusult2)
print("type(reusult2)=",type(reusult2))
# {'context': [Document(id='cf537a7e-48a9-43fe-b897-798f44aa841b', metadata={}, page_content='肘肘吃鸡蛋的时候用臀大肌夹碎鸡蛋'), Document(id='eb746d77-5810-443e-817d-2c93c587c58a', metadata={}, page_content='肘肘锻炼肩膀中枢的时候使用重力对抗系统增加难度'), Document(id='4266b502-df31-4fde-80ae-db5a634e334c', metadata={}, page_content='肘肘深蹲时候使用蛋气反重力系统')],
#  'question': '肘肘深蹲时候用的什么系统?'}
# chain1 = (
# # {"context": retriever, "question": RunnablePassthrough()}
#  {"context": retriever, "question": RunnablePassthrough()}
#     | prompt
#     | llm
#     | StrOutputParser()
# )
#
# result = chain1.invoke("肘肘深蹲时候用的什么系统?")
# print("result1",result)
# [HumanMessage(content="请根据以下语境回答问题:\n"
#                       "[Document(id='e770a6e8-0e23-4dba-95f8-3ef3640f27d1', metadata={}, "
#                       "page_content='肘肘深蹲时候使用蛋气反重力系统')]\n"
#                       "问题: 肘肘深蹲时候用的什么系统?\n",
#               additional_kwargs={}, response_metadata={})]


# Document 类型定义
# Document 是 LangChain 里用来封装文档数据的类，它通常包含两个主要属性：
# page_content：此属性为字符串类型，用于存储文档的具体内容。在你给出的例子中，page_content 包含了类似 “肘肘吃鸡蛋的时候用臀大肌夹碎鸡蛋” 这样的文本。
# metadata：这是一个字典类型的属性，用于存储与文档相关的元数据，像文档的来源、创建时间、作者等信息。在你的例子里，metadata 为空字典 {}，意味着没有额外的元数据被存储。
# id：这是文档的唯一标识符，在检索和管理文档时会用到。
# Document 的作用
# 1. 存储文档信息
# Document 能把文本内容和相关元数据组合成一个对象，方便在代码里进行管理和操作。例如，在你的代码中，向量数据库存储的就是 Document 对象列表，这样每个文本都能关联其对应的元数据和唯一标识符。
# 2. 检索和匹配
# 当使用检索器（如 retriever）从向量数据库中查找与问题相关的文档时，返回的结果就是 Document 对象列表。这样可以方便地获取文档的内容和元数据，为后续的处理提供依据。
# 3. 与大语言模型集成
# 在问答系统里，Document 对象的内容可以作为上下文信息传递给大语言模型，辅助模型生成更准确的回答。例如，在你的代码中，RunnableParallel 会把检索到的 Document 对象列表作为上下文信息传递给提示模板，然后再传递给大语言模型。