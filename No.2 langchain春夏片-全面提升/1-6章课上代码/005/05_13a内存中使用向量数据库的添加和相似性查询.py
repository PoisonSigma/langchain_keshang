from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from torch.utils.hipify.hipify_python import meta_data

# InMemoryVectorStore：把文档转化为向量并存储起来，进而实现快速的向量搜索。
# 自然语言处理
# 语义搜索：传统的文本搜索主要基于关键词匹配，而语义搜索则是基于文本的语义理解。向量数据库可以将文本转换为向量，通过计算向量之间的相似度，实现更精准的语义搜索。例如，在知识问答系统中，用户输入一个问题，系统可以在向量数据库中搜索与问题语义最相似的答案。
# 文本推荐：在新闻推荐、书籍推荐等场景中，向量数据库可以将文章、书籍等文本内容转换为向量，根据用户的历史阅读记录和兴趣偏好，推荐与之向量相似的文本内容。
# InMemoryVectorStore 是 LangChain 框架里的一个类，其主要功能是在内存里存储和管理向量数据。以下为你详细介绍它的作用和使用场景。



list1 = [
    "李阿姨说:这不是西格玛军儿吗?",
    "咋不说话了呢?军儿",
    "你不心中无女人,拔刀自然神吗?",
    "军儿说话啊?",
    "军说:我错了李阿姨?以后不敢装了,之前是我年少不知阿姨好,老了发现阿姨是块宝"
    ]
print(len(list1))
docs = []
for i in range(len(list1)):
    # print(list1[i])
    str1 = "语录"+str(i)
    # print(str1)
    docs.append(Document(page_content=list1[i],metadata = {"李阿姨的复仇":str1}))
# print(docs)
# vector_store = InMemoryVectorStore.from_documents(docs,HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))
vector_store = InMemoryVectorStore(HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))
vector_store.add_documents(docs) #添加记录
result = vector_store.similarity_search("老baby")#相似性搜索
for i in range(len(result)):
    print("第",i,"条记录:", result[i])


