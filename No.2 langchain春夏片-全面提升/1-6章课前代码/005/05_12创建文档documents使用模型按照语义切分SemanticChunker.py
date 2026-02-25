#SemanticChunker 会根据文本的语义关系来进行分割。

#SemanticChunker 基于语义进行文本分割，它会根据文本的语义相似度和嵌入向量来判断在哪里进行分割。在这个例子中，它将文本切分为两段，可能是因为模型认为前半部分（Aunt Li said, "Isn't this Juner from the Sigma group? Why aren't you saying anything? Don't you always say that when there is no woman in your heart, your swordsmanship will be naturally divine? Why aren't you talking now?"）和后半部分（Juner said, "I was wrong, Aunt Li. I won't act high and mighty like that anymore in the future. I was young before and didn't realize how wonderful you are, Auntie. Now that I'm older, I've found that you are truly a precious gem."）之间存在一定的语义差异，从而将它们分成了两个不同的语义块。具体的分割逻辑还会受到所使用的嵌入模型（all-MiniLM-L12-v2）以及模型对语义的理解和计算方式的影响。
from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

text_splitter = SemanticChunker(HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2"))


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
# 创建 Document 对象
docs = Document(page_content=strCn, metadata={"英文": "Poison 代码崩溃时的对白"})
split_docs = text_splitter.split_documents([docs])
count = 0
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

for doc in split_docs:
    count += 1
    print(doc.page_content,"count=",count)