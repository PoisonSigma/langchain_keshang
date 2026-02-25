import bs4
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
load_dotenv("../assets/openai.env")
from langchain_community.document_loaders import WebBaseLoader
# 设置环境变量，禁用 tokenizers 分词器 并行处理
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
url = "https://blog.csdn.net/boildoctor/article/details/121181152?spm=1001.2014.3001.5502"
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
splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=20)
split_documents = splitter.split_documents(docs)  # 分割器返回分割后的文档
print("split_documents=", split_documents)
for doc in split_documents:
    print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
    print(doc)


#HuggingFaceEmbeddings 抱脸虫可能会出现卡死的状态
 # 首次创建需要下载,以后就不用了,mac下的目录如下:
# ~/.cache/huggingface/hub

vectorstore = FAISS.from_documents(split_documents, embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"), )  # 通过分割后的小文档创建向量数据库
retriever = vectorstore.as_retriever()
#这里加一个打印,测试是否执行完vectorstore.as_retriever(),这部容易卡死,如果卡死,就删除HuggingFaceEmbeddings ,让他从新下载
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
# chain = {"retriever": retriever, "question": RunnablePassthrough()} | prompt
ai_msg = chain.invoke("内平栈相当于return以后栈再如何操作?")
print(ai_msg)
# [HumanMessage(content="\n    根据提供文档回答问题\n    "
#                       "[Document(id='de0994b3-b297-4579-9a47-09e39e62f1a5', metadata={'source': 'https://blog.csdn.net/boildoctor/article/details/121181152?spm=1001.2014.3001.5502'}, page_content='内平栈的特点是通过retn指令 改变esp，让栈平衡'), "
#                       "Document(id='4e3caf47-7d9f-4279-a78a-a033acd0dd7c', metadata={'source': 'https://blog.csdn.net/boildoctor/article/details/121181152?spm=1001.2014.3001.5502'}, page_content='栈平衡\\n内平栈'), "
#                       "Document(id='c98f21bf-c0a5-40cc-8bf8-fb967d3fd068', metadata={'source': 'https://blog.csdn.net/boildoctor/article/details/121181152?spm=1001.2014.3001.5502'}, page_content='出栈（call 结束后还原eip）call调用子程序retn 返回栈平衡内平栈外平栈'), "
#                       "Document(id='7690ab40-8735-486f-92f6-88cd075f8e43', metadata={'source': 'https://blog.csdn.net/boildoctor/article/details/121181152?spm=1001.2014.3001.5502'}, page_content='外平栈的retn 后面不跟着数字，而是在call结束以后在后面 add esp 直接增加 栈顶指针')]\n    下面是提出的问题:\n    内平栈相当于return以后栈再如何操作?\n    ", additional_kwargs={}, response_metadata={})]