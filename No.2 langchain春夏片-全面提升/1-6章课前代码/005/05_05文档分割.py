import bs4
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv("../assets/openai.env")
from langchain_community.document_loaders import WebBaseLoader

url = "https://blog.csdn.net/boildoctor/article/details/121181152?spm=1001.2014.3001.5502"
loader = WebBaseLoader(
    # (url,1)#不能这么给
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
# 这个默认是全家在
print("docs=", docs)
# Recursive 递归的
# Character字符
# Splitter分割器
# 创建分割器
# chunk_size 参数指定了每个文本块的最大字符数
# chunk_overlap,重叠字符数,可以确保相邻的文本块之间有一定的连贯性，避免信息的丢失。例如，在进行文本摘要或问答系统时，重叠的部分可以帮助模型更好地理解上下文，从而提高处理的准确性。
# 分割器,把loader读取过来的长文档,分解成小的短文档
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
split_documents = splitter.split_documents(docs)  # 分割器返回分割后的文档
print("split_documents=", split_documents)
for doc in split_documents:
    print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
    print(doc)

new_docs = []
# i = 0
# for doc in split_documents:
#     i+=1
#     print("i=",i)
#     if i > 10:
#         break
#     new_docs.append(doc)
#     print("向量数据库")
# for doc in new_docs:
#     print("doc=",doc)
# vectorstore = FAISS.from_documents(new_docs, embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"), )  # 通过分割后的小文档创建向量数据库
print("============")
# 指定本地模型路径
# mac本地路径
#~/.cache/huggingface/hub
# model_path = "~/.cache/huggingface/hub"
# embeddings = HuggingFaceEmbeddings(model_name=model_path)
#
# try:
#     vectorstore = FAISS.from_documents(split_documents, embedding=embeddings)
#     print("Vectorstore created successfully.")
# except Exception as e:
#     print(f"An error occurred: {e}")
vectorstore = FAISS.from_documents(split_documents, embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"), )  # 通过分割后的小文档创建向量数据库
print("============")
retriever = vectorstore.as_retriever()
print("============")
prompt = ChatPromptTemplate.from_template(
    """
    根据提供文档回答问题
    {retriever}
    下面是提出的问题:
    {question}
    """
)
# 管道操作符|强制转换,字典转并行 放在链里面可以省略外面的RunnableParallel ,而并行的执行结果还是个字典,可以传给下面的prompt当做invoke的参数
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
chain = {"retriever": retriever, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()
print("=======")
# chain = {"retriever": retriever, "question": RunnablePassthrough()} | prompt
# ai_msg = chain.invoke("内平栈相当于return以后栈再如何操作?")
# print("ai_msg=",ai_msg)