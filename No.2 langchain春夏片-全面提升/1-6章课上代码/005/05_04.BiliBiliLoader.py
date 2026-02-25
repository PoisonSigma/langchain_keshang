# ssl 证书查找的问题
#开发者模式里面查找cookie选配参数
#https://www.bilibili.com/video/BV1MuRZYsEmL
#https://python.langchain.com/api_reference/community/document_loaders.html
# 安装并配置证书库 ,解决错误ssl_shutdown_timeout
#解释器安装包: certifi
import os
import certifi #解决ssl证书问题
os.environ['SSL_CERT_FILE'] = certifi.where()
#需要安装包:解释器中安装:  bilibili-api-python
#%pip install --upgrade --quiet  bilibili-api-python
#或者用uv安装:uv add bilibili-api-python
bili_jct="4848c15a6bb3f35aee77521258045a60"
SESSDATA="2f729d39%2C1760267094%2C864de%2A41CjAG8RnGmsb4qKsb8lVsEskVlBpB2WEutNfv6RMZETCRyFANcbPMEvAsEwg_NHuIr-MSVnd1WHFSbEtybDM4Uzg0OHZyRTlxcWJjZlFTMzg2V2pCalctUE5Yd2ZkcGJQd0FxU3ZtdVBUQkV5Wm5jYTY3WFZxRlIyU2wwTGwtaWJDSXFmZkt3U2R3IIEC"
buvid3="F9CDE392-32DF-7ADE-20A3-F3930F5136B639898infoc"

from langchain_community.document_loaders import BiliBiliLoader
urls = [
    "https://www.bilibili.com/video/BV1MuRZYsEmL"
]
loader = BiliBiliLoader(
urls,
sessdata=SESSDATA,
    bili_jct=bili_jct,
    buvid3=buvid3,
)
docs = loader.load()
for doc in docs:
    print("页面内容")
    print(doc.page_content)
    print("元数据")
    print(doc.metadata)