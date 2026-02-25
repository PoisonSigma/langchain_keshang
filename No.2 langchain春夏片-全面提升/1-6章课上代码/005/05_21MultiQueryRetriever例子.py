from dotenv import load_dotenv
import os
# from langchain.retrievers.multi_query import MultiQueryRetriever, LineListOutputParser
from langchain_classic.retrievers.multi_query import MultiQueryRetriever, LineListOutputParser

from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
load_dotenv("../assets/openai.env")
from langchain_community.document_loaders import WebBaseLoader
import bs4
from langchain_text_splitters import RecursiveCharacterTextSplitter
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
#MultiQueryRetriever多重查询检索器
#这个东西本质是,调用大模型 ,和一个提示词模板,让大模型帮用户生成多个文档,
# 这个提示词是要求大模型突破用户的思维限制
#返回的是[Document]

#下面是整体 多重查询检索器,返回 文档一下,再放到链中的整体思维逻辑
# {
#     """
#     根据我给出的文档{docs}
#     回答我的问题{final_question}
#     """
# }
# chain = 提示词 | llm | 输出分析器
# chain.invoke({"docs":[Document],"final_question":"我最后想问一下,来时候的火车票,谁报给报销"})
url = "https://blog.csdn.net/boildoctor/article/details/123654243"
loader = WebBaseLoader(
    # (url,1)#不能这么给
    url,
    bs_kwargs={
        "parse_only": bs4.SoupStrainer(
            [
                "article" #这个标签的寻找方式,详见后面的视频课程:05_11手动筛选html网页源代码获取loader使用的标签
            ],
        )
    }
)
muti_retriever = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=40)
split_documents = splitter.split_documents(muti_retriever)  # 分割器返回分割后的文档
#创建向量数据库
embedding = HuggingFaceEmbeddings(model_name="shibing624/text2vec-base-chinese")
#嵌入的作用:是把自然语言文本转化到向量数据库中的过程
vectorstore = Chroma.from_documents(split_documents,embedding=embedding)
#创建检索器,相当于在检索器执行invoke时在向量数据库里面查询
retriever = vectorstore.as_retriever()
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
#多重查询检索器,返回的是一个文档list [Document]
muti_retriever = MultiQueryRetriever.from_llm(retriever, llm)#他的本质是一条链,执行的时候需要invoke,stream,
print("muti_retriever=", muti_retriever)
dic1 = muti_retriever.to_json()
import json
json_str = json.dumps(dic1, ensure_ascii=False, indent=2)
print("json_str=",json_str)
#默认的提示词模板占位符是:question
('You are an AI language model assistant. Your task is \n  '
 '  to generate 3 different versions of the given user \n   '
 ' question to retrieve relevant documents from a vector  database. \n   '
 ' By generating multiple perspectives on the user question, \n   '
 ' your goal is to help the user overcome some of the limitations \n   '
 ' of distance-based similarity search. Provide these alternative \n    '
 'questions separated by newlines. Original question: {question}')
# 是一名AI语言模型助手。
#你的任务是\n为给定用户\n生成3个不同的版本
#从向量数据库中检索相关文档。\ n
#通过对用户问题\n生成多个视角
#你的目标是帮助用户克服一些限制\n
#基于距离的相似性搜索。提供这些替代方案\n
#用换行符分隔问题。原始问题：{question} `)
docs = muti_retriever.invoke({"question":"如何把动态库安装到越狱手机上"})
print("docs=",docs)
print("type(docs)=",type(docs))
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
for doc in docs:
    print(doc)

prompt = ChatPromptTemplate.from_template("""
根据我提供的文档{docs}
回答问题{final_question}
""")
#LineListOutputParser把返回的结果 放到list里面 []
chain = prompt | llm | LineListOutputParser()
ai_msg = chain.invoke({"docs":docs,"final_question":"把动态库安装到越狱手机上和安装到普通手机上有哪些区别"})
print("ai_msg=",ai_msg)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

for doc in ai_msg:
    print(doc)

