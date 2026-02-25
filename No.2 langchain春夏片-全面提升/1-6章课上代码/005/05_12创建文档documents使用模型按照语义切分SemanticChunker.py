#官网的分割器的网址:
#https://python.langchain.com/api_reference/text_splitters/index.html#

#Semantic语义
#Chunker分析器
#SemanticChunker 通过训练模型创建的分割器
#安装包:langchain-experimental
from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings


strCn = """
李阿姨说:这不是西格玛军儿吗?
咋不说话了呢?
你不心中无女人,拔刀自然神吗?
咋不说话了呢?
军说:我错了李阿姨?以后不敢装了,之前是我年少不知阿姨好,老了发现阿姨是块宝
"""
strEn = """
Aunt Li said, "Isn't this Juner from the Sigma group?
Why aren't you saying anything?
Don't you always say that when there is no woman in your heart, your swordsmanship will be naturally divine?
Why aren't you talking now?"
Juner said, "I was wrong, Aunt Li. I won't act high and mighty like that anymore in the future. I was young before and didn't realize how wonderful you are, Auntie. Now that I'm older, I've found that you are truly a precious gem."
"""

doc = Document(page_content= strCn,meta_data ={"这是军儿代码崩溃时说的话":"不说话了"})
spliter = SemanticChunker(HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))
splite_docs = spliter.split_documents([doc])
count = 0
for doc in splite_docs:
    count += 1
    print("第",count,"行:",doc)