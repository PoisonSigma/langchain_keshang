
from langchain_core.documents import Document
#langchain-chroma
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

#生成检索器是为了统一调用接口,不需要每个向量数据库都单独写查询,retriever可以调用invoke查询
#嵌入Embedding 是把文本转向量的过程, 使用SemanticChunker语义分割器 和 创建向量数据库的时候要用
list1 = [
    "咋不说话了呢?",
    "李阿姨说:这不是西格玛军儿吗?",
    "你不心中无女人,拔刀自然神吗?",
    "说话啊军?",
    "军说:我错了李阿姨?以后不敢装了,之前是我年少不知阿姨好,老了发现阿姨是块宝",
    "怎样写好一份工作总结",
    "面试的时候应该注意什么",
    "如何与同事进行有效的沟通",
    "怎样提高工作效率",
    "职场晋升需要具备哪些能力",
]
#假设我们用WebBaseLoader .load()生成了一个文档list,这个过程我们用list自己生成一个文档

docs = []
for i in range(len(list1)):
    str1 = "对白"+str(i+1)
    docs.append(Document(page_content=list1[i], metadata={"对白": str1},id = str(i+1)))
for doc in docs:
    print(doc,end="")
    print(doc.id)
#上面是模拟用webbaseloader 读取并且分割文档
embedding = HuggingFaceEmbeddings(model_name="shibing624/text2vec-base-chinese")
#嵌入的作用:是把自然语言文本转化到向量数据库中的过程
vectorstore = Chroma.from_documents(docs,embedding=embedding)
retriever = vectorstore.as_retriever()
#检索器的作用是把统一化的操作
# ,把不同的数据库的查询都用检索器invoke解决
# result = retriever.invoke("工作")#这里检索器就相当于向量数据库的查询
result = retriever.invoke("军儿")#这里检索器就相当于向量数据库的查询
print(result)
#检索器在本地查询之后,把本地的大量文档变成搜索查询结果的文档,再发给大模型,可以优化使用llm的效率
