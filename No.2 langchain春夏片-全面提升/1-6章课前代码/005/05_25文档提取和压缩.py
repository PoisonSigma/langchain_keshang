#文档压缩的意义:让大模型帮忙减少容易文档,因为第一次的文档是向量数据库查询得来的文档

#LLMChainExtractor  提取器,本质是一个链,里面带着 让大模型 提取文档的默认提示词模板
#ContextualCompressionRetriever,上下文压缩检索器,传入参数要把前面的提取器,传进去,再传入完整的从网页读过来的文档,返回压缩后文档



import bs4
from langchain.chains import create_retrieval_chain
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

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
model_name="shibing624/text2vec-base-chinese"
embedding = HuggingFaceEmbeddings(model_name=model_name)#嵌入式把文本转换为向量的过程
vectorstore = Chroma.from_documents(documents=splits, embedding=embedding)
retriever = vectorstore.as_retriever()
print("retriever=",retriever)
#让检索器,查询向量数据库
docs = retriever.invoke("如何重签名")
print("docs=",docs)


from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
extractor = LLMChainExtractor.from_llm(llm)#基本压缩器
# llm_chain=PromptTemplate(input_variables=['context', 'question'], input_types={}, output_parser=NoOutputParser(), partial_variables={},
#                          template='Given the following question and context, extract any part of the context *AS IS* that is relevant to answer the question. If none of the context is relevant return NO_OUTPUT. \n\nRemember, *DO NOT* edit the extracted parts of the context.\n\n> Question: {question}\n> Context:\n>>>\n{context}\n>>>\nExtracted relevant parts:')
# | ChatDeepSeek(client=<openai.resources.chat.completions.completions.Completions object at 0x1725a06e0>, async_client=<openai.resources.chat.completions.completions.AsyncCompletions object at 0x1725ac440>, model_name='deepseek-chat', temperature=0.8, model_kwargs={}, api_key=SecretStr('**********'), api_base='https://api.deepseek.com/v1')
# | NoOutputParser() get_input=<function default_get_input at 0x14d4953a0>
#给下面的问题和上下文，提取上下文中与回答问题相关的任何部分。
# 如果上下文都不相关，则返回NO_OUTPUT。记住，不要修改上下文中提取的部分。
#提示词中的占位符是:Question: {question}\n> Context:\n>>>\n{context}
print("extractor=",extractor)
#ContextualCompressionRetriever 上下文压缩检索器
compression_retriever = ContextualCompressionRetriever(
    base_compressor=extractor, base_retriever=retriever
)
#这里base_compressor ,基础压缩给的是上面提取器的带提取提示词模板的链
#base_retriever是第一步,从网页读取过来检索器返回的全部完整结果
print("compression_retriever=",compression_retriever)

compression_docs = compression_retriever.invoke(
    "重签名是什么意思?"
)
print("compressed_docs:", compression_docs)
#得到压缩后的文档