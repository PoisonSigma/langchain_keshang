from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

# InMemoryVectorStore：把文档转化为向量并存储起来，进而实现快速的向量搜索。
# 自然语言处理
# 语义搜索：传统的文本搜索主要基于关键词匹配，而语义搜索则是基于文本的语义理解。向量数据库可以将文本转换为向量，通过计算向量之间的相似度，实现更精准的语义搜索。例如，在知识问答系统中，用户输入一个问题，系统可以在向量数据库中搜索与问题语义最相似的答案。
# 文本推荐：在新闻推荐、书籍推荐等场景中，向量数据库可以将文章、书籍等文本内容转换为向量，根据用户的历史阅读记录和兴趣偏好，推荐与之向量相似的文本内容。
# InMemoryVectorStore 是 LangChain 框架里的一个类，其主要功能是在内存里存储和管理向量数据。以下为你详细介绍它的作用和使用场景。
vector_store = InMemoryVectorStore(embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2"))

# 使用 all-MiniLM-L12-v2 这个预训练模型把文本转换为向量。all-MiniLM-L12-v2 是一个轻量级且高效的嵌入模型，能快速地将文本转换为向量。
from langchain_core.documents import Document

list1 = [
    "咋不说话了呢?",
    "李阿姨说:这不是西格玛军儿吗?",
    "你不心中无女人,拔刀自然神吗?",
    "说话啊军?",
    "军说:我错了李阿姨?以后不敢装了,之前是我年少不知阿姨好,老了发现阿姨是块宝"
]

docs = []
for item in list1:
    docs.append(Document(item, metadata={"source": "对白3"}))
for item in docs:
    print(item)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

vector_store.add_documents(docs)  # 把文档添加到向量数据库中
result_docs = vector_store.similarity_search("谁是块宝?")

print("result_docs=", result_docs)
for i in range(len(result_docs)):
    print(i, result_docs[i])
# print(result_docs)
