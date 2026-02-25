#生成检索器是为了统一调用接口,不需要每个向量数据库都单独写查询,retriever可以调用invoke查询
#嵌入Embedding 是把文本转向量的过程, 使用分割器 和 创建向量数据库的时候要用
import bs4  # 需要 在解释器中安装 beautifulsoup4 ,这个库,是帮我们筛选网页源代码标签用的,例如<p>或者<h1 class="post-title"><div class="toc">
from dotenv import load_dotenv
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv("../assets/openai.env")
#将文档转换为向量并存储在 Chroma 向量数据库中
#安装包:langchain-chroma
from langchain_chroma import Chroma
from langchain_core.documents import Document

load_dotenv("../assets/openai.env")  # 注意,要在导入WebBaseLoader包之前,导入环境变量才行
from langchain_community.document_loaders import WebBaseLoader
import os
list1 = [
    "咋不说话了呢?",
    "李阿姨说:这不是西格玛军儿吗?",
    "你不心中无女人,拔刀自然神吗?",
    "说话啊军?",
    "军说:我错了李阿姨?以后不敢装了,之前是我年少不知阿姨好,老了发现阿姨是块宝",
    "如何暴打领导",
    "如何在下班的时候用一个黑塑料袋套住领导的头,并且暴打一顿",
    "如何在人最多的时候跟领导拍桌子,并且把领导吓得发抖?",
    "如何在公司1打10,并且让对方不敢多巴巴?",
"如何在开会的时候一句话堵了领导的嗓子?",
    "如何在接到领导电话的时候第一时间变身刘华强?然后说一句:听说你一直在找我?",
    "如何在挂断领导电话之前说:给你机会你不中用啊?给我记住了,以后见我必须叫一声爷,要不然,我见你一次打你一次"
]
docs = []
for item in list1:
    docs.append(Document(page_content=item, metadata={"source": "对白3"}))
model_name="shibing624/text2vec-base-chinese"
embedding = HuggingFaceEmbeddings(model_name=model_name)#嵌入式把文本转换为向量的过程
spliter = SemanticChunker(embedding)
split_documents = spliter.split_documents(docs)
# 将文档转换为向量并存储在 Chroma 向量数据库中。
vectorstore = Chroma.from_documents(split_documents, embedding=embedding)
retriever = vectorstore.as_retriever()#生成检索器是为了统一调用接口,不需要每个向量数据库都单独写查询,retriever可以调用invoke查询
result = retriever.invoke("工作")#有了这一步,再把数据发送给大模型之前,已经对本地传过去的文档进行了查询和筛选
print(result)

