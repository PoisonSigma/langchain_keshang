#第一步,创建一个分割后的文档的检索器
import bs4
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.chat_message_histories import ChatMessageHistory
import os
load_dotenv("../assets/openai.env")
from langchain_community.document_loaders import WebBaseLoader
# 设置环境变量，禁用 tokenizers 分词器 并行处理
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
url = "https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501"
loader = WebBaseLoader(
    # (url,1)#不能这么给
    url,
    #捕获这种标签 <div class="detail hidden no-preview"
    bs_kwargs={
        "parse_only": bs4.SoupStrainer(
            [
                "div"
            ],
            attrs={"class": "detail hidden no-preview"}
        )
    }
)
docs = loader.load()
print("docs=", docs)
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
split_documents = splitter.split_documents(docs)  # 分割器返回分割后的文档
print("split_documents=", split_documents)
for doc in split_documents:
    print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
    print(doc)

embedding = HuggingFaceEmbeddings(model_name = "BAAI/bge-m3")#北京智源人工智能研究院 出的
vectorstore = FAISS.from_documents(split_documents, embedding=embedding)  # 通过分割后的小文档创建向量数据库
retriever = vectorstore.as_retriever()
# ;一.创建历史聊天感知链检索器:history_aware_retriever
# 历史聊天记录chat_history,或者叫上下文,都行
# 1.定义一个上下文(历史聊天记录)的系统提示词,这个是给后面整体提示词中,的system角色用的
context_sys_prompt = """
给定一段聊天记录以及用户提出的最新问题，
该问题可能会引用聊天记录中的上下文信息。
请构建一个独立的问题，使其在没有聊天记录的情况下也能被理解。
如果有必要，对问题进行重新表述，否则就按原样返回该问题。
"""
history_prompt = ChatPromptTemplate.from_messages(
[
        ("system", context_sys_prompt),
        ("placeholder", "{chat_history}"),  # 这里放历史聊天记录,如果有的话就放这里,这个历史记录,第一次使用的时候是没有的,但是也能被感知到
        ("human", "{input}"),  # 这里是最终的用户输入,是多轮对话,每次用户输入的新问题
    ]
)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
# 3.创建历史感知检索器,用来检查是否输入了聊天历史记录,
# 本质上,是分支结构,里面会判断最终invoke输入的字典是否包含input 和chat_history,
# 其中chat_history可以不包含
history_aware_retriever = create_history_aware_retriever(llm,retriever,history_prompt)
print("history_aware_retriever=", history_aware_retriever)
# 二.创建用户输入的问题链:question_answer_chain
question_msg = """
你是一个负责问答任务的助手。
使用以下检索到的上下文信息来回答问题。
如果你不知道答案，就说你不知道。
最多使用三句话，并且回答要简洁明了。
{context}
"""
# 注意这里要有{context},否则报错ValueError: Prompt must accept context as an input variable. Received prompt with input variables: ['input']
qustion_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", question_msg),
        ("placeholder", "{chat_history}"),  # 这里放历史聊天记录,如果有的话就放这里
        ("human", "{input}"),  # 这里是最终的用户输入
    ]
)
# 跟上面的历史链一样,也需要传入input和 chat_history,但是多了一个context,作用是接收上下文和历史聊天记录,并且查询答案
#创建问题链
qustion_chain = create_stuff_documents_chain(llm,qustion_prompt)
print("qustion_chain=", qustion_chain)
# 三.生成检索链create_retrieval_chain
rag_chain = create_retrieval_chain(history_aware_retriever,qustion_chain)
# 这个字典用来存储聊天历史的id,因为字典里面如果键值重复会存不进去
store = {}
def get_session_history(session_id:str):#这个是传入的id
    print("session_id=", session_id)
    if session_id not in store:
        print("ChatMessageHistory=", ChatMessageHistory())
        store[session_id]    = ChatMessageHistory()# 在内存中实现聊天消息的历史记录。 将消息存储在内存列表中。
        print("store[session_id]=",store[session_id]   )
    print("store=",store)
    return store[session_id]

final_chain = RunnableWithMessageHistory(
    rag_chain,
get_session_history,
input_messages_key = "input",
output_messages_key =  "answer", #这个必须是answer
history_messages_key = "chat_history"
)
result1 = final_chain.invoke({"input":"创建远程线程是什么意思?"},config={"configurable": {"session_id": "001"}})
print("result1=", result1)
print("result1 answer=", result1["answer"])
result2 = final_chain.invoke({"input":"给我用C++实现一下?"},config={"configurable": {"session_id": "001"}})
print("result2=", result2)
print("result2=", result2["answer"])
result3 = final_chain.invoke({"input":"给我用一个其他语言实现一下?"},config={"configurable": {"session_id": "001"}})
print("result3=", result3)
print("result3=", result3["answer"])
# get_session_history: GetSessionHistoryCallable,
# *,
# input_messages_key: Optional[str] = None,
# output_messages_key: Optional[str] = None,
# history_messages_key: Optional[str] = None,

# config={"configurable": {"session_id": "bar"}

