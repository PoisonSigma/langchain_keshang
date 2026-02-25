# RAG 是 “Retrieval-Augmented Generation” 的缩写，即检索增强生成
import bs4
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv("../assets/openai.env")
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

os.environ['TOKENIZERS_PARALLELISM'] = 'false'
def rag_fun(url ,bs_kwargs,question):
    # 标签article
    loader = WebBaseLoader(
        url,
        bs_kwargs=bs_kwargs
    )
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)
    model_name = "shibing624/text2vec-base-chinese"
    embedding = HuggingFaceEmbeddings(model_name=model_name)  # 嵌入式把文本转换为向量的过程
    vectorstore = Chroma.from_documents(documents=splits, embedding=embedding)
    retriever = vectorstore.as_retriever()
    print("retriever=", retriever)
    # 让检索器,查询向量数据库
    from langchain.retrievers import ContextualCompressionRetriever
    from langchain.retrievers.document_compressors import LLMChainExtractor
    import os
    from langchain_deepseek import ChatDeepSeek
    from dotenv import load_dotenv
    load_dotenv("../assets/openai.env")
    llm = ChatDeepSeek(
        model=os.getenv("MODEL_NAME"),
        temperature=0.8)
    extractor = LLMChainExtractor.from_llm(llm)  # 基本压缩器
    # ContextualCompressionRetriever 上下文压缩检索器
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=extractor, base_retriever=retriever
    )
    compression_docs = compression_retriever.invoke(
        question
    )
    result = compression_retriever.invoke(question)
    print("压缩后返回的文档是=", result)
    for i in range(len(result)):
        print(str(i), " :", result[i].page_content)
    # 得到压缩后的文档
    prmpt = ChatPromptTemplate.from_template("""
    根据我给出的文档
    {compression_docs}
    回答问题:{question}
    """)
    prmpt_result = prmpt.invoke({"question": question,"compression_docs":compression_docs})
    print("prmpt_result=",prmpt_result)
    chain = prmpt | llm | StrOutputParser()
    ai_msg = chain.invoke({"question": question,"compression_docs":compression_docs})
    print("ai_msg=", ai_msg)
url = "https://blog.csdn.net/boildoctor/article/details/123654243"
bs_kwargs = {
            "parse_only": bs4.SoupStrainer(
                [
                    "article"
                ],
            )
        }
question = "重签名是什么意思?"
rag_fun(url, bs_kwargs, question)
