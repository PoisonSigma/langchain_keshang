#下面是官网所有loader的api文档
#https://python.langchain.com/api_reference/community/document_loaders.html
from langchain_community.document_loaders import BiliBiliLoader

#需要安装包:解释器中安装:  bilibili-api-python

#%pip install --upgrade --quiet  bilibili-api-python
# 填写你要获取字幕的哔哩哔哩视频的 URL

# 安装并配置证书库
#解释器安装包: certifi
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()


from langchain_community.document_loaders import BiliBiliLoader
video_urls = [
    "https://www.bilibili.com/video/BV1MuRZYsEmL"
]
#下面3个参数看笔记里面B站获取参数.md 里面看截图和文字的获取方法
SESSDATA = "2f729d39%2C1760267094%2C864de%2A41CjAG8RnGmsb4qKsb8lVsEskVlBpB2WEutNfv6RMZETCRyFANcbPMEvAsEwg_NHuIr-MSVnd1WHFSbEtybDM4Uzg0OHZyRTlxcWJjZlFTMzg2V2pCalctUE5Yd2ZkcGJQd0FxU3ZtdVBUQkV5Wm5jYTY3WFZxRlIyU2wwTGwtaWJDSXFmZkt3U2R3IIEC"
BUVID3 = "F9CDE392-32DF-7ADE-20A3-F3930F5136B639898infoc"
BILI_JCT = "4848c15a6bb3f35aee77521258045a60"

# 初始化 BiliBiliLoader
loader = BiliBiliLoader(
    video_urls=video_urls,
    sessdata=SESSDATA,
    bili_jct=BILI_JCT,
    buvid3=BUVID3
)

# 加载数据
docs = loader.load()

# 打印获取到的文档内容
for doc in docs:
    print(doc.page_content)
    print("Metadata:")#Metadata 指的是与所加载的哔哩哔哩视频相关的元数据。元数据属于描述数据的数据，在这个情境中，它涵盖了视频的各种属性与信息，例如视频的基本信息、统计数据、分区信息等
    print(doc.metadata)