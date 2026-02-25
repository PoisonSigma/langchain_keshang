#第一步,创建一个分割后的文档的检索器
import bs4
from dotenv import load_dotenv
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.history_aware_retriever import create_history_aware_retriever
from langchain_classic.chains.retrieval import create_retrieval_chain
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
#session_id相同的情况,store里面的key存储一个session_id,但是里面对应的value,会改变,
# 每次都是存储最新的完整的历史聊天记录,这个记录会放在整个链当中,发给大模型,
# 进行最新的提问
store = {}
def get_session_history(session_id:str):#这个是传入的id
    print("session_id=", session_id)
    if session_id not in store:#如果对应的id不同,就不保存到新的key里面,
        # 例如这个例子,所有session_id都是001,那么就只给字典创建一个key:001
        print("ChatMessageHistory=", ChatMessageHistory())
        store[session_id]    = ChatMessageHistory()# 在内存中实现聊天消息的历史记录。 将消息存储在内存列表中。
        print("store[session_id] =",store[session_id]   )
    print("store=",store)
    return store[session_id]

final_chain = RunnableWithMessageHistory(
    rag_chain,
get_session_history,
#下面3行直接复制
input_messages_key = "input",
output_messages_key =  "answer", #这个必须是answer
history_messages_key = "chat_history"
)
result1 = final_chain.invoke({"input":"创建远程线程是什么意思?"},config={"configurable": {"session_id": "001"}})
print("result1=", result1)
print("result1 answer=", result1["answer"])
result2 = final_chain.invoke({"input":"给我用C++实现一下?"},config={"configurable": {"session_id": "002"}})
print("result2=", result2)
print("result2=", result2["answer"])
result3 = final_chain.invoke({"input":"给我用一个其他语言实现一下?"},config={"configurable": {"session_id": "001"}})
print("result3=", result3)
print("result3=", result3["answer"])

# def chat_withHistory(shuoCi:str):
#     final_chain.invoke({"input":shuoCi},config={"configurable": {"session_id": "001"}})
# result4 =  chat_withHistory("对不起,我没有计算机,我只有算盘子,请问,怎么学习ai大模型")
# get_session_history: GetSessionHistoryCallable,
# *,
# input_messages_key: Optional[str] = None,
# output_messages_key: Optional[str] = None,
# history_messages_key: Optional[str] = None,

# config={"configurable": {"session_id": "bar"}

# result1= {'input': '创建远程线程是什么意思?', 'chat_history': [], 'context': [Document(id='70e0f873-e9e0-4c1a-9bd8-bc3b81565a9a', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='3. **创建线程**：使用`CreateRemoteThread`函数在目标进程中创建一个新的线程，该线程会执行你在步骤2中写入的`LoadLibrary` API调用，从而加载DLL。\n\n4. **处理回调**：一旦DLL被成功加载，它的`DllMain`函数会被调用，你可以在这里执行自定义的初始化逻辑。如果你的DLL需要执行特定的操作，比如注册导出函数，这一步至关重要。'), Document(id='57d80bd4-e785-429f-bca0-055db0f5311d', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='DLL（Dynamic Link Library）是Windows操作系统中的一个重要组成部分，它是一种可重用的代码库，能够被多个应用程序同时调用，以实现共享功能和资源。DLL注入技术是指将一个DLL文件加载到目标进程的地址空间中，使得该DLL的代码可以在目标进程中执行。这种技术在系统调试、性能监测、插件开发以及恶意软件中都有应用。'), Document(id='672a0402-de55-4972-9a4c-3237bd34480d', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='DLL注入是Windows编程中的一项高级技术，它涉及到进程间通信、内存管理和系统调用等多个方面。理解和掌握DLL注入，可以帮助开发者更深入地理解操作系统的工作机制，并且在特定情况下实现一些高级功能。但同时，也要意识到其可能带来的安全问题，合理使用这项技术。'), Document(id='28562d1c-82dc-43dd-a2d9-5e62bdf1f1ac', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='2. **加载DLL**：接下来，你需要使用`VirtualAllocEx`函数在目标进程的地址空间中分配内存，用于存放DLL的路径和加载DLL的API调用（如`LoadLibraryA`或`LoadLibraryW`）。然后，使用`WriteProcessMemory`函数将这些数据写入目标进程。')], 'answer': '创建远程线程是指在目标进程中创建一个新的线程，使其执行指定的代码。通常用于DLL注入，例如使用`CreateRemoteThread`函数让目标进程加载DLL。这样可以实现在目标进程中运行自定义代码的目的。'}
# result2= {'input': '给我用C++实现一下?', 'chat_history': [HumanMessage(content='创建远程线程是什么意思?', additional_kwargs={}, response_metadata={}), AIMessage(content='创建远程线程是指在目标进程中创建一个新的线程，使其执行指定的代码。通常用于DLL注入，例如使用`CreateRemoteThread`函数让目标进程加载DLL。这样可以实现在目标进程中运行自定义代码的目的。', additional_kwargs={}, response_metadata={})], 'context': [Document(id='6ec62e6e-d8e5-4ade-88d7-b0ae0787bf6e', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='我们要理解DLL注入的基本原理。当一个进程启动时，它可以加载指定的DLL文件。但是，DLL注入则是在进程运行过程中，通过编程手段动态地将DLL加载到目标进程中。这一过程通常包括以下几个步骤：\n\n1. **获取进程句柄**：你需要知道目标进程的进程ID，然后使用`OpenProcess`函数获取该进程的句柄，这允许你对目标进程进行操作。'), Document(id='672a0402-de55-4972-9a4c-3237bd34480d', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='DLL注入是Windows编程中的一项高级技术，它涉及到进程间通信、内存管理和系统调用等多个方面。理解和掌握DLL注入，可以帮助开发者更深入地理解操作系统的工作机制，并且在特定情况下实现一些高级功能。但同时，也要意识到其可能带来的安全问题，合理使用这项技术。'), Document(id='28562d1c-82dc-43dd-a2d9-5e62bdf1f1ac', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='2. **加载DLL**：接下来，你需要使用`VirtualAllocEx`函数在目标进程的地址空间中分配内存，用于存放DLL的路径和加载DLL的API调用（如`LoadLibraryA`或`LoadLibraryW`）。然后，使用`WriteProcessMemory`函数将这些数据写入目标进程。'), Document(id='70e0f873-e9e0-4c1a-9bd8-bc3b81565a9a', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='3. **创建线程**：使用`CreateRemoteThread`函数在目标进程中创建一个新的线程，该线程会执行你在步骤2中写入的`LoadLibrary` API调用，从而加载DLL。\n\n4. **处理回调**：一旦DLL被成功加载，它的`DllMain`函数会被调用，你可以在这里执行自定义的初始化逻辑。如果你的DLL需要执行特定的操作，比如注册导出函数，这一步至关重要。')], 'answer': '以下是一个简单的 C++ 示例，演示如何使用 `CreateRemoteThread` 进行 DLL 注入：  \n\n```cpp\n#include <windows.h>\n#include <tlhelp32.h>\n#include <iostream>\n\nbool InjectDLL(DWORD processId, const char* dllPath) {\n    // 1. 打开目标进程\n    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, processId);\n    if (!hProcess) {\n        std::cerr << "OpenProcess failed: " << GetLastError() << std::endl;\n        return false;\n    }\n\n    // 2. 在目标进程分配内存，存放DLL路径\n    LPVOID remoteMem = VirtualAllocEx(hProcess, NULL, strlen(dllPath) + 1, MEM_COMMIT, PAGE_READWRITE);\n    if (!remoteMem) {\n        std::cerr << "VirtualAllocEx failed: " << GetLastError() << std::endl;\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 3. 写入DLL路径到目标进程\n    if (!WriteProcessMemory(hProcess, remoteMem, dllPath, strlen(dllPath) + 1, NULL)) {\n        std::cerr << "WriteProcessMemory failed: " << GetLastError() << std::endl;\n        VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 4. 获取LoadLibraryA地址（在目标进程中调用）\n    LPVOID loadLibAddr = (LPVOID)GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA");\n    if (!loadLibAddr) {\n        std::cerr << "GetProcAddress failed" << std::endl;\n        VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 5. 创建远程线程执行LoadLibraryA\n    HANDLE hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE)loadLibAddr, remoteMem, 0, NULL);\n    if (!hThread) {\n        std::cerr << "CreateRemoteThread failed: " << GetLastError() << std::endl;\n        VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 6. 等待线程执行完毕\n    WaitForSingleObject(hThread, INFINITE);\n\n    // 7. 清理资源\n    VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n    CloseHandle(hThread);\n    CloseHandle(hProcess);\n\n    return true;\n}\n\nint main() {\n    DWORD pid = 1234; // 替换为目标进程ID\n    const char* dllPath = "C:\\\\path\\\\to\\\\your.dll"; // 替换为DLL路径\n\n    if (InjectDLL(pid, dllPath)) {\n        std::cout << "DLL injected successfully!" << std::endl;\n    } else {\n        std::cerr << "DLL injection failed." << std::endl;\n    }\n\n    return 0;\n}\n```\n\n### 注意事项：\n1. **管理员权限**：需要以管理员身份运行，否则可能无法打开目标进程。  \n2. **目标进程位数**：确保你的注入程序和目标进程的位数（32/64位）匹配，否则会失败。  \n3. **DLL路径**：确保DLL路径正确，否则 `LoadLibrary` 会失败。  \n\n如果需要更详细的解释或调试，可以进一步讨论！'}
# result3= {'input': '给我用一个其他语言实现一下?', 'chat_history': [HumanMessage(content='创建远程线程是什么意思?', additional_kwargs={}, response_metadata={}), AIMessage(content='创建远程线程是指在目标进程中创建一个新的线程，使其执行指定的代码。通常用于DLL注入，例如使用`CreateRemoteThread`函数让目标进程加载DLL。这样可以实现在目标进程中运行自定义代码的目的。', additional_kwargs={}, response_metadata={}), HumanMessage(content='给我用C++实现一下?', additional_kwargs={}, response_metadata={}), AIMessage(content='以下是一个简单的 C++ 示例，演示如何使用 `CreateRemoteThread` 进行 DLL 注入：  \n\n```cpp\n#include <windows.h>\n#include <tlhelp32.h>\n#include <iostream>\n\nbool InjectDLL(DWORD processId, const char* dllPath) {\n    // 1. 打开目标进程\n    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, processId);\n    if (!hProcess) {\n        std::cerr << "OpenProcess failed: " << GetLastError() << std::endl;\n        return false;\n    }\n\n    // 2. 在目标进程分配内存，存放DLL路径\n    LPVOID remoteMem = VirtualAllocEx(hProcess, NULL, strlen(dllPath) + 1, MEM_COMMIT, PAGE_READWRITE);\n    if (!remoteMem) {\n        std::cerr << "VirtualAllocEx failed: " << GetLastError() << std::endl;\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 3. 写入DLL路径到目标进程\n    if (!WriteProcessMemory(hProcess, remoteMem, dllPath, strlen(dllPath) + 1, NULL)) {\n        std::cerr << "WriteProcessMemory failed: " << GetLastError() << std::endl;\n        VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 4. 获取LoadLibraryA地址（在目标进程中调用）\n    LPVOID loadLibAddr = (LPVOID)GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA");\n    if (!loadLibAddr) {\n        std::cerr << "GetProcAddress failed" << std::endl;\n        VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 5. 创建远程线程执行LoadLibraryA\n    HANDLE hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE)loadLibAddr, remoteMem, 0, NULL);\n    if (!hThread) {\n        std::cerr << "CreateRemoteThread failed'

# store= {'001': InMemoryChatMessageHistory(messages=[])}
# store= {'001': InMemoryChatMessageHistory(messages=[HumanMessage(content='创建远程线程是什么意思?', additional_kwargs={}, response_metadata={}), AIMessage(content='创建远程线程是指在目标进程中创建一个新的线程，使其执行指定的代码。通常用于DLL注入，例如使用`CreateRemoteThread`函数让目标进程加载DLL。这样可以实现在目标进程中运行自定义代码的目的。', additional_kwargs={}, response_metadata={})])}
# store= {'001': InMemoryChatMessageHistory(messages=[HumanMessage(content='创建远程线程是什么意思?', additional_kwargs={}, response_metadata={}), AIMessage(content='创建远程线程是指在目标进程中创建一个新的线程，使其执行指定的代码。通常用于DLL注入，例如使用`CreateRemoteThread`函数让目标进程加载DLL。这样可以实现在目标进程中运行自定义代码的目的。', additional_kwargs={}, response_metadata={}), HumanMessage(content='给我用C++实现一下?', additional_kwargs={}, response_metadata={}), AIMessage(content='以下是一个简单的 C++ 示例，演示如何使用 `CreateRemoteThread` 进行 DLL 注入：  \n\n```cpp\n#include <windows.h>\n#include <tlhelp32.h>\n#include <iostream>\n\nbool InjectDLL(DWORD processId, const char* dllPath) {\n    // 1. 打开目标进程\n    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, processId);\n    if (!hProcess) {\n        std::cerr << "OpenProcess failed: " << GetLastError() << std::endl;\n        return false;\n    }\n\n    // 2. 在目标进程分配内存，存放DLL路径\n    LPVOID remoteMem = VirtualAllocEx(hProcess, NULL, strlen(dllPath) + 1, MEM_COMMIT, PAGE_READWRITE);\n    if (!remoteMem) {\n        std::cerr << "VirtualAllocEx failed: " << GetLastError() << std::endl;\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 3. 写入DLL路径到目标进程\n    if (!WriteProcessMemory(hProcess, remoteMem, dllPath, strlen(dllPath) + 1, NULL)) {\n        std::cerr << "WriteProcessMemory failed: " << GetLastError() << std::endl;\n        VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 4. 获取LoadLibraryA地址（在目标进程中调用）\n    LPVOID loadLibAddr = (LPVOID)GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA");\n    if (!loadLibAddr) {\n        std::cerr << "GetProcAddress failed" << std::endl;\n        VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 5. 创建远程线程执行LoadLibraryA\n    HANDLE hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE)loadLibAddr, remoteMem, 0, NULL);\n    if (!hThread) {\n        std::cerr << "CreateRemoteThread failed: " << GetLastError() << std::endl;\n        VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 6. 等待线程执行完毕\n    WaitForSingleObject(hThread, INFINITE);\n\n    // 7. 清理资源\n    VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n    CloseHandle(hThread);\n    CloseHandle(hProcess);\n\n    return true;\n}\n\nint main() {\n    DWORD pid = 1234; // 替换为目标进程ID\n    const char* dllPath = "C:\\\\path\\\\to\\\\your.dll"; // 替换为DLL路径\n\n    if (InjectDLL(pid, dllPath)) {\n        std::cout << "DLL injected successfully!" << std::endl;\n    } else {\n        std::cerr << "DLL injection failed." << std::endl;\n    }\n\n    return 0;\n}\n```\n\n### 注意事项：\n1. **管理员权限**：需要以管理员身份运行，否则可能无法打开目标进程。  \n2. **目标进程位数**：确保你的注入程序和目标进程的位数（32/64位）匹配，否则会失败。  \n3. **DLL路径**：确保DLL路径正确，否则 `LoadLibrary` 会失败。  \n\n如果需要更详细的解释或调试，可以进一步讨论！', additional_kwargs={}, response_metadata={})])}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ': " << GetLastError() << std::endl;\n        VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n        CloseHandle(hProcess);\n        return false;\n    }\n\n    // 6. 等待线程执行完毕\n    WaitForSingleObject(hThread, INFINITE);\n\n    // 7. 清理资源\n    VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);\n    CloseHandle(hThread);\n    CloseHandle(hProcess);\n\n    return true;\n}\n\nint main() {\n    DWORD pid = 1234; // 替换为目标进程ID\n    const char* dllPath = "C:\\\\path\\\\to\\\\your.dll"; // 替换为DLL路径\n\n    if (InjectDLL(pid, dllPath)) {\n        std::cout << "DLL injected successfully!" << std::endl;\n    } else {\n        std::cerr << "DLL injection failed." << std::endl;\n    }\n\n    return 0;\n}\n```\n\n### 注意事项：\n1. **管理员权限**：需要以管理员身份运行，否则可能无法打开目标进程。  \n2. **目标进程位数**：确保你的注入程序和目标进程的位数（32/64位）匹配，否则会失败。  \n3. **DLL路径**：确保DLL路径正确，否则 `LoadLibrary` 会失败。  \n\n如果需要更详细的解释或调试，可以进一步讨论！', additional_kwargs={}, response_metadata={})], 'context': [Document(id='28562d1c-82dc-43dd-a2d9-5e62bdf1f1ac', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='2. **加载DLL**：接下来，你需要使用`VirtualAllocEx`函数在目标进程的地址空间中分配内存，用于存放DLL的路径和加载DLL的API调用（如`LoadLibraryA`或`LoadLibraryW`）。然后，使用`WriteProcessMemory`函数将这些数据写入目标进程。'), Document(id='6ec62e6e-d8e5-4ade-88d7-b0ae0787bf6e', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='我们要理解DLL注入的基本原理。当一个进程启动时，它可以加载指定的DLL文件。但是，DLL注入则是在进程运行过程中，通过编程手段动态地将DLL加载到目标进程中。这一过程通常包括以下几个步骤：\n\n1. **获取进程句柄**：你需要知道目标进程的进程ID，然后使用`OpenProcess`函数获取该进程的句柄，这允许你对目标进程进行操作。'), Document(id='70e0f873-e9e0-4c1a-9bd8-bc3b81565a9a', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='3. **创建线程**：使用`CreateRemoteThread`函数在目标进程中创建一个新的线程，该线程会执行你在步骤2中写入的`LoadLibrary` API调用，从而加载DLL。\n\n4. **处理回调**：一旦DLL被成功加载，它的`DllMain`函数会被调用，你可以在这里执行自定义的初始化逻辑。如果你的DLL需要执行特定的操作，比如注册导出函数，这一步至关重要。'), Document(id='672a0402-de55-4972-9a4c-3237bd34480d', metadata={'source': 'https://download.csdn.net/download/boildoctor/802404?spm=1001.2014.3001.5501'}, page_content='DLL注入是Windows编程中的一项高级技术，它涉及到进程间通信、内存管理和系统调用等多个方面。理解和掌握DLL注入，可以帮助开发者更深入地理解操作系统的工作机制，并且在特定情况下实现一些高级功能。但同时，也要意识到其可能带来的安全问题，合理使用这项技术。')], 'answer': '### **Python 实现 DLL 注入（使用 `ctypes` 调用 Windows API）**\n```python\nimport ctypes\nfrom ctypes import wintypes\n\n# 定义 Windows API 函数\nkernel32 = ctypes.WinDLL(\'kernel32\', use_last_error=True)\n\nOpenProcess = kernel32.OpenProcess\nOpenProcess.argtypes = (wintypes.DWORD, wintypes.BOOL, wintypes.DWORD)\nOpenProcess.restype = wintypes.HANDLE\n\nVirtualAllocEx = kernel32.VirtualAllocEx\nVirtualAllocEx.argtypes = (wintypes.HANDLE, wintypes.LPVOID, ctypes.c_size_t, wintypes.DWORD, wintypes.DWORD)\nVirtualAllocEx.restype = wintypes.LPVOID\n\nWriteProcessMemory = kernel32.WriteProcessMemory\nWriteProcessMemory.argtypes = (wintypes.HANDLE, wintypes.LPVOID, wintypes.LPCVOID, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t))\nWriteProcessMemory.restype = wintypes.BOOL\n\nGetProcAddress = kernel32.GetProcAddress\nGetProcAddress.argtypes = (wintypes.HMODULE, wintypes.LPCSTR)\nGetProcAddress.restype = wintypes.LPVOID\n\nGetModuleHandleA = kernel32.GetModuleHandleA\nGetModuleHandleA.argtypes = (wintypes.LPCSTR,)\nGetModuleHandleA.restype = wintypes.HMODULE\n\nCreateRemoteThread = kernel32.CreateRemoteThread\nCreateRemoteThread.argtypes = (wintypes.HANDLE, ctypes.POINTER(wintypes.SECURITY_ATTRIBUTES), ctypes.c_size_t, wintypes.LPVOID, wintypes.LPVOID, wintypes.DWORD, ctypes.POINTER(wintypes.DWORD))\nCreateRemoteThread.restype = wintypes.HANDLE\n\nWaitForSingleObject = kernel32.WaitForSingleObject\nWaitForSingleObject.argtypes = (wintypes.HANDLE, wintypes.DWORD)\nWaitForSingleObject.restype = wintypes.DWORD\n\nCloseHandle = kernel32.CloseHandle\nCloseHandle.argtypes = (wintypes.HANDLE,)\nCloseHandle.restype = wintypes.BOOL\n\n# 常量定义\nPROCESS_ALL_ACCESS = 0x1F0FFF\nMEM_COMMIT = 0x1000\nPAGE_READWRITE = 0x04\n\ndef inject_dll(pid, dll_path):\n    try:\n        # 1. 打开目标进程\n        h_process = OpenProcess(PROCESS_ALL_ACCESS, False, pid)\n        if not h_process:\n            raise ctypes.WinError(ctypes.get_last_error())\n\n        # 2. 在目标进程分配内存\n        remote_mem = VirtualAllocEx(h_process, None, len(dll_path) + 1, MEM_COMMIT, PAGE_READWRITE)\n        if not remote_mem:\n            raise ctypes.WinError(ctypes.get_last_error())\n\n        # 3. 写入DLL路径到目标进程\n        written = ctypes.c_size_t(0)\n        if not WriteProcessMemory(h_process, remote_mem, dll_path.encode(\'utf-8\'), len(dll_path) + 1, ctypes.byref(written)):\n            raise ctypes.WinError(ctypes.get_last_error())\n\n        # 4. 获取 LoadLibraryA 地址\n        kernel32_handle = GetModuleHandleA(b"kernel32.dll")\n        load_library_addr = GetProcAddress(kernel32_handle, b"LoadLibraryA")\n        if not load_library_addr:\n            raise ctypes.WinError(ctypes.get_last_error())\n\n        # 5. 创建远程线程执行 LoadLibraryA\n        thread_id = wintypes.DWORD(0)\n        h_thread = CreateRemoteThread(h_process, None, 0, load_library_addr, remote_mem, 0, ctypes.byref(thread_id))\n        if not h_thread:\n            raise ctypes.WinError(ctypes.get_last_error())\n\n        # 6. 等待线程执行完毕\n        WaitForSingleObject(h_thread, -1)\n\n        # 7. 清理资源\n        CloseHandle(h_thread)\n        CloseHandle(h_process)\n\n        print("DLL injected successfully!")\n        return True\n\n    except Exception as e:\n        print(f"Error: {e}")\n        return False\n\n# 使用示例\nif __name__ == "__main__":\n    target_pid = 1234  # 替换为目标进程ID\n    dll_path = "C:\\\\path\\\\to\\\\your.dll"  # 替换为DLL路径\n    inject_dll(target_pid, dll_path)\n```\n\n### **C# 实现 DLL 注入（使用 P/Invoke）**\n```csharp\nusing System;\nusing System.Diagnostics;\nusing System.Runtime.InteropServices;\n\nclass DLLInjector\n{\n    [DllImport("kernel32.dll", SetLastError = true)]\n    static extern IntPtr OpenProcess(int dwDesiredAccess, bool bInheritHandle, int dwProcessId);\n\n    [DllImport("kernel32.dll", SetLastError = true)]\n    static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);\n\n    [DllImport("kernel32.dll", SetLastError = true)]\n    static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress, byte[] lpBuffer, uint nSize, out IntPtr lpNumberOfBytesWritten);\n\n    [DllImport("kernel32.dll", SetLastError = true)]\n    static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, out IntPtr lpThreadId);\n\n    [DllImport("kernel32.dll", SetLastError = true)]\n    static extern IntPtr GetProcAddress(IntPtr hModule, string procName);\n\n    [DllImport("kernel32.dll", SetLastError = true)]\n    static extern IntPtr GetModuleHandle(string lpModuleName);\n\n    [DllImport("kernel32.dll", SetLastError = true)]\n    static extern uint WaitForSingleObject(IntPtr hHandle, uint dwMilliseconds);\n\n    [DllImport("kernel32.dll", SetLastError = true)]\n    static extern bool CloseHandle(IntPtr hObject);\n\n    const int PROCESS_ALL_ACCESS = 0x1F0FFF;\n    const uint MEM_COMMIT = 0x1000;\n    const uint PAGE_READWRITE = 0x04;\n\n    public static bool InjectDLL(int pid, string dllPath)\n    {\n        try\n        {\n            // 1. 打开目标进程\n            IntPtr hProcess = OpenProcess(PROCESS_ALL_ACCESS, false, pid);\n            if (hProcess == IntPtr.Zero)\n                throw new Exception($"OpenProcess failed: {Marshal.GetLastWin32Error()}");\n\n            // 2. 在目标进程分配内存\n            IntPtr remoteMem = VirtualAllocEx(hProcess, IntPtr.Zero, (uint)dllPath.Length + 1, MEM_COMMIT, PAGE_READWRITE);\n            if (remoteMem == IntPtr.Zero)\n                throw new Exception($"VirtualAllocEx failed: {Marshal.GetLastWin32Error()}");\n\n            // 3. 写入DLL路径\n            byte[] dllBytes = System.Text.Encoding.ASCII.GetBytes(dllPath);\n            IntPtr bytesWritten;\n            if (!WriteProcessMemory(hProcess, remoteMem, dllBytes, (uint)dllBytes.Length, out bytesWritten))\n                throw new Exception($"WriteProcessMemory failed: {Marshal.GetLastWin32Error()}");\n\n            // 4. 获取 LoadLibraryA 地址\n            IntPtr kernel32 = GetModuleHandle("kernel32.dll");\n            IntPtr loadLibAddr = GetProcAddress(kernel32, "LoadLibraryA");\n            if (loadLibAddr == IntPtr.Zero)\n                throw new Exception($"GetProcAddress failed: {Marshal.GetLastWin32Error()}");\n\n            // 5. 创建远程线程\n            IntPtr threadId;\n            IntPtr hThread = CreateRemoteThread(hProcess, IntPtr.Zero, 0, loadLibAddr, remoteMem, 0, out threadId);\n            if (hThread == IntPtr.Zero)\n                throw new Exception($"CreateRemoteThread failed: {Marshal.GetLastWin32Error()}");\n\n            // 6. 等待线程执行完毕\n            WaitForSingleObject(hThread, 0xFFFFFFFF);\n\n            // 7. 清理资源\n            CloseHandle(hThread);\n            CloseHandle(hProcess);\n\n            Console.WriteLine("DLL injected successfully!");\n            return true;\n        }\n        catch (Exception ex)\n        {\n            Console.WriteLine($"Error: {ex.Message}");\n            return false;\n        }\n    }\n\n    static void Main()\n    {\n        int targetPid = 1234; // 替换为目标进程ID\n        string dllPath = @"C:\\path\\to\\your.dll"; // 替换为DLL路径\n        InjectDLL(targetPid, dllPath);\n    }\n}\n```\n\n### **总结**\n- **Python** 使用 `ctypes` 调用 Windows API，适合快速测试。  \n- **C#** 使用 P/Invoke，代码更清晰，适合 .NET 开发。  \n- **C++** 是原生实现，性能最佳，适合底层开发。  \n\n如果你需要其他语言（如 Rust、Go 或 PowerShell），可以告诉我！'}

