# RAG 是 “Retrieval-Augmented Generation” 的缩写，即检索增强生成
from dotenv import load_dotenv
import os

from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
load_dotenv("../assets/openai.env")
from langchain_community.document_loaders import WebBaseLoader
import bs4
from langchain_text_splitters import RecursiveCharacterTextSplitter
os.environ['TOKENIZERS_PARALLELISM'] = 'false'

def rag_fun(url,tag,question):

    loader = WebBaseLoader(
        url,
        bs_kwargs={
            "parse_only": bs4.SoupStrainer(
                [
                    tag  # 这个标签的寻找方式,详见后面的视频课程:05_11手动筛选html网页源代码获取loader使用的标签
                ],
            )
        }
    )
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=40)
    split_documents = splitter.split_documents(docs)  # 分割器返回分割后的文档
    # 创建向量数据库
    embedding = HuggingFaceEmbeddings(model_name="shibing624/text2vec-base-chinese")
    # 嵌入的作用:是把自然语言文本转化到向量数据库中的过程
    vectorstore = Chroma.from_documents(split_documents, embedding=embedding)
    # retriever = vectorstore.as_retriever(search_type="mmr", #搜索类型mmr最大边际相关性
    #             search_kwargs={'k': 6, 'lambda_mult': 0.25}) #lambda_mult越接近1,越准确,体现相关性,越接近0越多样性
    retriever = vectorstore.as_retriever()
    # 创建检索器,相当于在检索器执行invoke时在向量数据库里面查询
    import os
    from langchain_deepseek import ChatDeepSeek
    from dotenv import load_dotenv
    load_dotenv("../assets/openai.env")
    llm = ChatDeepSeek(
        model=os.getenv("MODEL_NAME"),
        temperature=0.8)
    # 创建提取器,压缩器
    extractor = LLMChainExtractor.from_llm(llm)
    compression_retriever = ContextualCompressionRetriever(base_compressor=extractor, base_retriever=retriever)

    result_compression_docs = compression_retriever.invoke("重签名是什么?")
    print("压缩后返回的文档是:")
    for i in range(len(result_compression_docs)):
        print(str(i), " :", result_compression_docs[i].page_content)
    prompt = ChatPromptTemplate.from_template("""
    根据我给出的文档:
    {result_compression_docs}
    回答问题:{question}
    """)
    chain =  prompt | llm | StrOutputParser()
    ai_msg = chain.invoke({"result_compression_docs":result_compression_docs, "question":question})#这样不行,result_compression_docs是list不是Runnable
    # chain ={"result_compression_docs": result_compression_docs, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()
    # ai_msg = chain.invoke(question)
    print("ai_msg",ai_msg)
url = "https://blog.csdn.net/boildoctor/article/details/123654243"
tag = "article"
question = "重签名是什么意思?"
rag_fun(url,tag,question)