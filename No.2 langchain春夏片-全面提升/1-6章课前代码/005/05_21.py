
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv("../assets/openai.env")
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEmbeddings
import bs4
from langchain_text_splitters import RecursiveCharacterTextSplitter
# 设置环境变量，禁用 tokenizers 并行处理
import os
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
url = "https://blog.csdn.net/boildoctor/article/details/123654243"
#标签article
loader =  WebBaseLoader(
    url,
    bs_kwargs={
        "parse_only": bs4.SoupStrainer(
            [
                "article"
            ],
        )
    }
)
docs = loader.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splite_docs = text_splitter.split_documents(docs)
model_name="shibing624/text2vec-base-chinese"
embedding = HuggingFaceEmbeddings(model_name=model_name)#嵌入式把文本转换为向量的过程
# VectorDB
vectorstrore = Chroma.from_documents(documents=splite_docs, embedding=embedding)
retriever = vectorstrore.as_retriever()
print(retriever)
print(retriever.invoke("把越狱手机上自制的动态库安装到普通手机上"))
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

                                    # print(retriever.retrieve("zh"))
                                    # print(retriever.retrieve("en"))
                                    # print(retriever.retrieve("zh"))

from langchain.retrievers.multi_query import MultiQueryRetriever


import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)

question = "如何重签名?"

retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=retriever, llm=llm
)
#MultiQueryRetriever自带一个提示词模板
# template='
# You are an AI language model assistant.
# Your task is \n    to generate 3 different versions of the given user \n
# question to retrieve relevant documents from a vector  database. \n
# By generating multiple perspectives on the user question, \n
# your goal is to help the user overcome some of the limitations \n
# of distance-based similarity search. Provide these alternative \n
# questions separated by newlines. Original question: {question}')
# 是一名AI语言模型助手。
#你的任务是\n为给定用户\n生成3个不同的版本
#从向量数据库中检索相关文档。\ n
#通过对用户问题\n生成多个视角
#你的目标是帮助用户克服一些限制\n
#基于距离的相似性搜索。提供这些替代方案\n
#用换行符分隔问题。原始问题：{question} `)
dic1 = retriever_from_llm.to_json()
import json
json_retriever =json.dumps(dic1, ensure_ascii=False, indent=2)
print("json_retriever=",json_retriever)
print("retriever_from_llm=",retriever_from_llm)
#这个MultiQueryRetriever本身就带着 链,链里面有 提示词模板,输入的占位符默认是question,和输出分析器,LineListOutputParser()
#LineListOutputParser() 是按行分割的输出分析器
result_docs = retriever_from_llm.invoke(question)
for item in result_docs:
    print(item)
    print(type(item))

#返回结果是一个文档的列表list
#创建最终要生成的链:
prmpt1 = ChatPromptTemplate.from_template("""
根据文档{docs}
回答问题{final_question}
""")
chain = prmpt1 | llm | StrOutputParser()
final_result = chain.invoke({"docs":result_docs,"final_question":"把越狱手机上自制的动态库安装到普通手机上和安装到越狱手机上的区别?"})
print("final_result",final_result)