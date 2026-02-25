#抱脸的官网,下面是免费的bge m3
# BAAI/bge-m3
#https://huggingface.co/BAAI/bge-m3
from langchain_community.vectorstores import Chroma
#硅基流动模型官网
#https://siliconflow.cn/zh-cn/models
from langchain_huggingface import HuggingFaceEmbeddings
from nltk.data import retrieve

# 配置SiliconFlow嵌入模型
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",  #北京智源人工智能研究院 出的
)
print("模型嵌入完毕")
# 使用示例
text = "欢迎使用SiliconFlow!"
query_result = embeddings.embed_query(text)  # 单个文本嵌入
print("query_result=",query_result)
doc_result = embeddings.embed_documents([text])  # 批量文本嵌入
print("doc_result=",doc_result)
list1 = ["中国人民银行",
         "中国人民很行",
         "中国农业银行",
         "中国工商银行",
         "你放屁很臭",
         "你放屁香"
                   ]
vectorstore = Chroma.from_texts(list1,embedding = embeddings)
retriever = vectorstore.as_retriever(search_kwargs={'k': 3})
docs =  retriever.invoke("不吃香菜")
print(docs)
for doc in docs:
    print(doc)
