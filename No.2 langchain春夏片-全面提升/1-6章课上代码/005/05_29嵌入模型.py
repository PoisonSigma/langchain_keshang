#抱脸的官网,下面是免费的bge m3
# BAAI/bge-m3
#pro BAAI/bge-m3 ,硅基流动,0.7
#https://huggingface.co/BAAI/bge-m3
 # 首次创建需要下载,以后就不用了,mac下的目录如下:
# ~/.cache/huggingface/hub
#硅基流动模型官网
#https://siliconflow.cn/zh-cn/models
#腾讯云的 向量数据库 ,按照小时付费 0.78 元 ,或者是按月付费 150
#嵌入模型,token 0.7
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name = "BAAI/bge-m3")#北京智源人工智能研究院 出的
list1 = ["中国人民银行",
         "中国人民很行",
         "中国农业银行",
         "中国工商银行",
         "你放屁很臭",
         "你放屁香",
         "蛋白屁",
         "蛋清屁",
         "淡黄色气体"
                   ] #令老外发指

vectorstore = Chroma.from_texts(list1,embedding = embedding)
print("向量数据库创建完毕")
docs = vectorstore.similarity_search_with_score("",k = 5)
for doc in docs:
    print(doc)