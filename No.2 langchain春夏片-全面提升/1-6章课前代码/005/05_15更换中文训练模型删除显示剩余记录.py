from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

# 使用 shibing624/text2vec-base-chinese 这个预训练模型把文本转换为向量。
# shibing624/text2vec-base-chinese 是一个对中文处理较好的嵌入模型
# 首次创建需要下载,以后就不用了,mac下的目录如下:
# ~/.cache/huggingface/hub
vector_store = InMemoryVectorStore(embedding=HuggingFaceEmbeddings(model_name="shibing624/text2vec-base-chinese"))

list1 = [
    "咋不说话了呢?",
    "李阿姨说:这不是西格玛军儿吗?",
    "你不心中无女人,拔刀自然神吗?",
    # "说话啊军?",
    # "军说:我错了李阿姨?以后不敢装了,之前是我年少不知阿姨好,老了发现阿姨是块宝",
    # "怎样写好一份工作总结",
    # "面试的时候应该注意什么",
    # "如何与同事进行有效的沟通",
    # "怎样提高工作效率",
    # "职场晋升需要具备哪些能力",
]

docs = []
# for item in list1:
#     docs.append(Document(page_content=item, metadata={"source": "对白3"}))
# for item in docs:
#     print(item)
docs.append(Document(page_content="测试对白4", metadata={"source": "测试"}))
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

vector_store.add_documents(docs)  # 把文档添加到向量数据库中
result_docs = vector_store.similarity_search("心中无女人会怎么样")
print("result_docs=", result_docs)
for i in range(len(result_docs)):
    print(i, result_docs[i])

result_docs = vector_store.similarity_search("工作相关")
print("工作相关,result_docs=", result_docs)
for i in range(len(result_docs)):
    print(i, result_docs[i])

result_docs = vector_store.similarity_search("工作相关", k=2)  # 只列出2条记录
print("工作相关,k=2 result_docs=", result_docs)
for i in range(len(result_docs)):
    print(i, result_docs[i])


def filter_fun(doc):  # 定义一个过滤函数
    return doc.metadata.get("source") == "测试"

result_docs = vector_store.similarity_search("工作相关", filter=filter_fun)  # 最多列出2条记录,并且过滤器是自定义的函数filter_fun
print("工作相关,k=2 result_docs=", result_docs)
for i in range(len(result_docs)):
    print(i, result_docs[i])

# 假设这里有一个存在的 ID，你可以根据实际情况修改
vector_store.delete(id='354ed121-7137-4169-a5e1-65bed31cfad7')  # 删除一个

# 获取并打印 vector_store 中剩余的文档
remaining_docs = vector_store.similarity_search("",len(vector_store.store))
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
for i in range(len(remaining_docs)):
    print(i, remaining_docs[i])