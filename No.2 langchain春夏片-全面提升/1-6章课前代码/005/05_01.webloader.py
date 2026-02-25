import os

import bs4  # 需要 在解释器中安装 beautifulsoup4

# 这个是WebBaseLoader在网页所在服务器发送请求的时候发给服务器的
# openai.env 里面添加上USER_AGENT 可以不显示此警告
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma, FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv("../assets/openai.env")  # 注意,要在导入WebBaseLoader包之前,导入环境变量才行
# print(os.getenv("USER_AGENT"))
# 如果不导入环境变量USER_AGENT,运行会提示USER_AGENT environment variable not set, consider setting it to identify your requests.
from langchain_community.document_loaders import WebBaseLoader

# 仅保留博客文章中的标题、页眉和内容部分


import os

os.environ[
    'USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# url = "https://lilianweng.github.io/posts/2023-06-23-agent/"
url = "http://47.93.135.183"
loader = WebBaseLoader(
    web_paths=(url,),  # 注意这个后面的逗号要有
    bs_kwargs=
    dict(
        parse_only=bs4.SoupStrainer(
            # [
            #     "p",
            #     "h1",
            #     # "div"
            #     {"name": "div", "attrs": {"class": "prompt"}} #嵌套会出现警告
            # ],
            name=["p", "h1", "div"],
            attrs={"class": "prompt"} if "p" in ["div"] else {}
            # class_ = "prompt"
            # bs_kwargs 是一个字典，用于存储传递给 BeautifulSoup 解析器的额外参数。WebBaseLoader 会把这些参数传递给 BeautifulSoup，以此来定制解析过程。
        ),  # parse_only 是 BeautifulSoup 解析器的一个参数，它的作用是指定解析器仅解析满足特定条件的 HTML 元素，这样能提升解析效率，尤其是在处理大型 HTML 文档时。
    )  # bs_kwargs 是一个字典，用于存储传递给 BeautifulSoup 解析器的额外参数。WebBaseLoader 会把这些参数传递给 BeautifulSoup，以此来定制解析过程。
)  # parse_only 是 BeautifulSoup 解析器的一个参数，它的作用是指定解析器仅解析满足特定条件的 HTML 元素，这样能提升解析效率，尤其是在处理大型 HTML 文档时。

docs = loader.load()
print("docs=", docs)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

splits = text_splitter.split_documents(docs)
vectorstore = FAISS.from_documents(documents=splits,
                                   embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2"),

                                   )
retriever = vectorstore.as_retriever()
print("retriever=", retriever)

result = retriever.invoke("我自行车坏了")
print("result=", result)
