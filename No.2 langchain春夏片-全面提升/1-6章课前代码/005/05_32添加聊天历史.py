from dotenv import load_dotenv
import os

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnableWithMessageHistory
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from numexpr.necompiler import context_info

load_dotenv("../assets/openai.env")
from langchain_community.document_loaders import WebBaseLoader
import bs4
from langchain_text_splitters import RecursiveCharacterTextSplitter

os.environ['TOKENIZERS_PARALLELISM'] = 'false'
url = "https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501"

loader = WebBaseLoader(
    url,
    bs_kwargs={
        # 要捕获的标签是 <div class="detail hidden no-preview"
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
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
split_documents = splitter.split_documents(docs)  # 分割器返回分割后的文档
# 创建向量数据库
embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")  # 北京智源人工智能研究院 出的
# 嵌入的作用:是把自然语言文本转化到向量数据库中的过程
vectorstore = Chroma.from_documents(split_documents, embedding=embedding)
# 创建检索器,相当于在检索器执行invoke时在向量数据库里面查询
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
# from_messages 第一个参数要的是一个list []\
# 2.创建上下文的提示词,context_prompt上下文的提示词,还是用来传入历史聊天记录的
context_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", context_sys_prompt),
        ("placeholder", "{chat_history}"),  # 这里放历史聊天记录,如果有的话就放这里
        ("human", "{input}"),  # 这里是最终的用户输入
    ]
)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
# 3.创建历史感知检索器,用来检查是否输入了聊天历史记录,本质上,是分支结构,里面会判断最终invoke输入的字典是否包含input 和chat_history,其中chat_history可以不包含
history_aware_retriever = create_history_aware_retriever(llm, retriever, context_prompt)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

print("history_aware_retriever=", history_aware_retriever)
# 1.先把文档分割后生成新的检索器
# result1 = history_aware_retriever.invoke({"input":"内存注入式什么?"})#不带chat_history的调用
# chat_history_list = [
#     "内存注入是一个windows核心编程的技术",
#     "内存注入可以不需要知道别人写的程序的源代码,就能让别人的程序调用自己写的代码"
# ]
# result1 = history_aware_retriever.invoke(
#     {"input": "内存注入式什么?", "chat_history2": chat_history_list})  # 不带chat_history的调用
# #lambda x: not x.get('chat_history', False) ,字典里面如果有chat_history,就返回false
# #字典里面有聊天记录,就返回Ture,没有,取默认值False,再取反=等于有聊天记录就是False,没有就是Ture
# print("result1=", result1)
# print("=============")
# # 链1返回了4个文档
# for doc in result1:
#     print(doc.page_content)
# 简单来说下面会 通过输入的字典 里面是否有 chat_history 和 input进行操作
# RunnableBranch(branches=[
#     (RunnableLambda(lambda x: not x.get('chat_history', False)),
#      RunnableLambda(lambda x: x['input'])
# | VectorStoreRetriever(tags=['Chroma', 'HuggingFaceEmbeddings'], vectorstore=<langchain_chroma.vectorstores.Chroma object at 0x14f492a50>, search_kwargs={}))],
# default=ChatPromptTemplate(input_variables=['input'], optional_variables=['chat_history'], input_types={'chat_history': list[typing.Annotated[typing.Union[typing.Annotated[langchain_core.messages.ai.AIMessage, Tag(tag='ai')], typing.Annotated[langchain_core.messages.human.HumanMessage, Tag(tag='human')], typing.Annotated[langchain_core.messages.chat.ChatMessage, Tag(tag='chat')], typing.Annotated[langchain_core.messages.system.SystemMessage, Tag(tag='system')], typing.Annotated[langchain_core.messages.function.FunctionMessage, Tag(tag='function')], typing.Annotated[langchain_core.messages.tool.ToolMessage, Tag(tag='tool')], typing.Annotated[langchain_core.messages.ai.AIMessageChunk, Tag(tag='AIMessageChunk')], typing.Annotated[langchain_core.messages.human.HumanMessageChunk, Tag(tag='HumanMessageChunk')], typing.Annotated[langchain_core.messages.chat.ChatMessageChunk, Tag(tag='ChatMessageChunk')], typing.Annotated[langchain_core.messages.system.SystemMessageChunk, Tag(tag='SystemMessageChunk')], typing.Annotated[langchain_core.messages.function.FunctionMessageChunk, Tag(tag='FunctionMessageChunk')], typing.Annotated[langchain_core.messages.tool.ToolMessageChunk, Tag(tag='ToolMessageChunk')]], FieldInfo(annotation=NoneType, required=True, discriminator=Discriminator(discriminator=<function _get_type at 0x105bece00>, custom_error_type=None, custom_error_message=None, custom_error_context=None))]]}, partial_variables={'chat_history': []}, messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=[], input_types={}, partial_variables={}, template='\n给定一段聊天记录以及用户提出的最新问题，\n该问题可能会引用聊天记录中的上下文信息。\n请构建一个独立的问题，使其在没有聊天记录的情况下也能被理解。\n如果有必要，对问题进行重新表述，否则就按原样返回该问题。\n'), additional_kwargs={}), MessagesPlaceholder(variable_name='chat_history', optional=True), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], input_types={}, partial_variables={}, template='{input}'), additional_kwargs={})])
# | ChatDeepSeek(client=<openai.resources.chat.completions.completions.Completions object at 0x172df8980>, async_client=<openai.resources.chat.completions.completions.AsyncCompletions object at 0x172e04590>, model_name='deepseek-chat', temperature=0.8, model_kwargs={}, api_key=SecretStr('**********'), api_base='https://api.deepseek.com/v1')
# | StrOutputParser()
# | VectorStoreRetriever(tags=['Chroma', 'HuggingFaceEmbeddings'], vectorstore=<langchain_chroma.vectorstores.Chroma object at 0x14f492a50>, search_kwargs={})) kwargs={} config={'run_name': 'chat_retriever_chain'} config_factories=[]

# 二.创建用户输入的问题链:question_answer_chain
question_msg = """
你是一个负责问答任务的助手。
使用以下检索到的上下文信息来回答问题。
如果你不知道答案，就说你不知道。
最多使用三句话，并且回答要简洁明了。
 {context}
"""
# 注意这里要有{context},否则报错
qustion_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", question_msg),
        ("placeholder", "{chat_history}"),  # 这里放历史聊天记录,如果有的话就放这里
        ("human", "{input}"),  # 这里是最终的用户输入
    ]
)
# 跟上面的历史链一样,也需要传入input和 chat_history,但是多了一个context,作用是接收上下文和历史聊天记录,并且查询答案
qustion_chain = create_stuff_documents_chain(llm, qustion_prompt)
print("qustion_chain=", qustion_chain)
# 三.生成检索链create_retrieval_chain
rag_chain = create_retrieval_chain(history_aware_retriever, qustion_chain)
store = {}  # 这个字典用来存储聊天历史的id,因为字典里面如果键值重复会存不进去


def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()  # 在内存中实现聊天消息的历史记录。 将消息存储在内存列表中。
        print("store[session_id]=", store[session_id])
    return store[session_id]  # 把存储之后的id返回


final_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,  # 参数2要一个Callable函数名
    input_messages_key="input",
    output_messages_key="answer",  #这里的输出的key,不能改,否则报错
    history_messages_key="chat_history"
)
result1 = final_chain.invoke({"input": "创建远程线程是什么意思??"}, config={
    "configurable": {"session_id": "123"}
}
)
print("final_chain=",final_chain)
print("result1=", result1)
result2 = final_chain.invoke({"input": "提供一下C++代码"}, config={
    "configurable": {"session_id": "123"}
}
)
result3 = final_chain.invoke({"input": "这段代码的不用C++可以写吗?用其他语言呢?"}, config={
    "configurable": {"session_id": "123"}
})
print("result2=", result2)
print("result3=", result3)
print("result2 answer=", result2["answer"])
print("result3 answer=", result3["answer"])
# {'input': '提供一下代码', 'chat_history':
#     [HumanMessage(content='创建远程线程是什么意思??', additional_kwargs={}, response_metadata={}),
#      AIMessage(content='创建远程线程是指在另一个进程（目标进程）中创建一个新的线程来执行代码。这通常用于将DLL注入到目标进程中，使其代码能在该进程内运行。常用于调试、监控或恶意软件等场景。', additional_kwargs={}, response_metadata={})],
#  'context': [Document(id='bbca20ff-c131-47d2-8c99-0818130f3db4', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'},
#                       page_content='3. **创建线程**：使用`CreateRemoteThread`函数在目标进程中创建一个新的线程，该线程会执行你在步骤2中写入的`LoadLibrary` API调用，从而加载DLL。'),
#              Document(id='418e1199-c759-42ca-928a-c51d3f543356', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'},
#                       page_content='**加载DLL**：接下来，你需要使用`VirtualAllocEx`函数在目标进程的地址空间中分配内存，用于存放DLL的路径和加载DLL的API调用（如`LoadLibraryA`或`LoadLi'),
#              Document(id='02956a0a-5fe2-4a40-abab-fa269d1efbbe', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'},
#                       page_content='个DLL文件加载到目标进程的地址空间中，使得该DLL的代码可以在目标进程中执行。这种技术在系统调试、性能监测、插件开发以及恶意软件中都有应用。'),
#              Document(id='fc74f7b3-6da1-4d2f-9a93-89e97a55abf8', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'},
#                       page_content='我们要理解DLL注入的基本原理。当一个进程启动时，它可以加载指定的DLL文件。但是，DLL注入则是在进程运行过程中，通过编程手段动态地将DLL加载到目标进程中。这一过程通常包括以下几个步骤：')],
#  'answer': '以下是使用 `CreateRemoteThread` 进行 DLL 注入的简单代码示例（C++）：  \n\n```cpp\n// 目标进程 ID 和 DLL 路径\nDWORD pid = 1234;  \nconst char* dllPath = "C:\\\\example.dll";  \n\n// 1. 打开目标进程  \nHANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);  \n\n// 2. 在目标进程分配内存存放 DLL 路径  \nLPVOID pDllPath = VirtualAllocEx(hProcess, NULL, strlen(dllPath) + 1, MEM_COMMIT, PAGE_READWRITE);  \n\n// 3. 写入 DLL 路径  \nWriteProcessMemory(hProcess, pDllPath, dllPath, strlen(dllPath) + 1, NULL);  \n\n// 4. 获取 LoadLibraryA 地址（Kernel32.dll 在所有进程中地址相同）  \nLPVOID pLoadLibrary = (LPVOID)GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA");  \n\n// 5. 创建远程线程执行 LoadLibraryA  \nHANDLE hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE)pLoadLibrary, pDllPath, 0, NULL);  \n\n// 6. 清理句柄  \nCloseHandle(hThread);  \nCloseHandle(hProcess);  \n```  \n\n**注意**：此代码仅用于学习，滥用可能违反安全策略或法律。'}
