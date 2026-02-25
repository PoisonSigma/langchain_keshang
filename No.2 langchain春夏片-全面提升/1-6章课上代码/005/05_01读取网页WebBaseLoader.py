import bs4  # 需要 在解释器中安装 beautifulsoup4 ,这个库,是帮我们筛选网页源代码标签用的,例如<p>或者<h1 class="post-title"><div class="toc">
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
# 这个是WebBaseLoader在网页所在服务器发送请求的时候发给服务器的
# openai.env 里面添加上USER_AGENT 可以不显示此警告,
# 这个环境变量要加载在WebBaseLoader 这个包引入之前
from langchain_community.document_loaders import WebBaseLoader

url = "http://47.93.135.183"
# url = "https://lilianweng.github.io/posts/2023-06-23-agent/"
# loader = WebBaseLoader(url).load() #这个默认是全家在
loader = WebBaseLoader(
    # (url,1)#不能这么给
    url,
    # bs_kwargs=dict(parse_only=bs4.SoupStrainer(
    #     [
    #         "h1",
    #         "p",
    #         # 找一个这个标签的<div class="inner">
    #         "div"
    #     ],

    bs_kwargs={
        "parse_only": bs4.SoupStrainer(
            # "h1",#可以单独传一个
            [
                "h1",
                "p",
                # 找一个这个标签的<div class="inner">
                "div"
                # {"name": "div", "attrs": {"class": "prompt"}}  # 嵌套会出现警告
            ],
            # attrs={"class": "post-title"}
            # attrs=dict(class = "prompt")#错误,class 是关键字
        )
    }

).load()  # 这个默认是全家在
print("loader=", loader)

# dic1 = {"name": "张三", "age": 18}
# print("dic1=", dic1)
# print("dic1=", type(dic1))
# dic2 = dict(name="张三", age=18)  # 这个也是创建字典
# print("dic2=", dic2)
# print("dic2=", type(dic2))
