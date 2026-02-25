import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

# SemanticSimilarityExampleSelector
# Semantic语义
# Similarity相似性
# 核心选择策略差异
# SemanticSimilarityExampleSelector
# 策略：该选择器基于语义相似度来挑选示例。它会计算输入文本与每个示例文本之间的语义相似度得分，然后选择得分最高的 k 个示例。
# 特点：简单直接，能确保选择的示例与输入在语义上最为接近，适用于需要紧密围绕输入主题的场景。例如，在进行近义词查询时，它会优先选择与输入词语语义最相似的示例。
from langchain_core.example_selectors import SemanticSimilarityExampleSelector

# 核心选择策略差异
# SemanticSimilarityExampleSelector
# 策略：该选择器基于语义相似度来挑选示例。它会计算输入文本与每个示例文本之间的语义相似度得分，然后选择得分最高的 k 个示例。
# 特点：简单直接，能确保选择的示例与输入在语义上最为接近，适用于需要紧密围绕输入主题的场景。例如，在进行近义词查询时，它会优先选择与输入词语语义最相似的示例。
# MaxMarginalRelevanceExampleSelector
# 策略：采用最大边际相关性（MMR）算法进行示例选择。MMR 算法不仅考虑示例与输入的相关性，还会考虑示例之间的多样性。它在选择示例时，会尽量保证所选示例既与输入相关，又能覆盖不同的方面，避免选择过于相似的示例。
# 特点：能在保证相关性的同时，提高示例的多样性。在一些需要综合考虑多方面信息的场景中非常有用，比如文本生成、问答系统等，可避免模型输出过于单一。
#
#  适用场景差异
# SemanticSimilarityExampleSelector
# 适用于对语义相关性要求极高，需要聚焦于特定主题的场景。例如，在进行法律条文的解释、医学术语的查询等任务时，需要选择与输入语义最接近的示例来确保准确性。
# MaxMarginalRelevanceExampleSelector
# 更适合需要综合多方面信息、提高输出多样性的场景。比如在创意写作、多领域知识问答等场景中，选择多样化的示例可以帮助模型生成更全面、更丰富的内容。

# 总结MMR 最大边际相关性,不仅有相似性,还有多样性,而SemanticSimilarity主要是取相似性
# 设置环境变量，禁用 tokenizers 分词器 并行处理
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
examples = [
    {"i": "苹果", "o": "水果"},
    {"i": "香蕉", "o": "水果"},
    {"i": "汽车", "o": "交通工具"},
    {"i": "自行车", "o": "交通工具"},
    {"i": "猫", "o": "动物"},
    {"i": "狗", "o": "动物"},
    {"i": "蛋白粉", "o": "营养补剂"},
    {"i": "蛋清粉", "o": "助推燃料"},
    {"i": "蛋白粉味的玉米粉", "o": "碳水"},
    {"i": "蛋白粉味的砖头粉", "o": "要你命三千"},
{"i": "那我 问你", "o": "语气助词,或者喘不上气了开始思考"},
]
# examples: list[dict],
#         embeddings: Embeddings,
#         vectorstore_cls: type[VectorStore],
selector = SemanticSimilarityExampleSelector.from_examples(

    # 创建 Hugging Face 嵌入模型
    # 首次创建需要下载,以后就不用了,mac下的目录如下:~/.cache/huggingface/hub
    # HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
    embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2"),
    examples=examples,
    # 使用了 句子变形金刚Sentence Transformers
    # all-MiniLM-L12-v2 和 all-MiniLM-L6-v2 一样，其生成的嵌入向量维度都是 384 维。
    # all-MiniLM-L12-v2 是 Sentence Transformers 库中的一个预训练模型，它基于 MiniLM 架构，该模型经过专门训练，可以将文本转换为固定长度的向量表示，这个向量的维度就是 384 维。在进行语义相似度计算、文本聚类、信息检索等任务时，模型会把输入的文本编码成 384 维的向量，然后基于这些向量进行后续的操作。
    # Sentence Transformers 是一个用于生成句子和文本嵌入（embeddings）的 Python 库，它在自然语言处理（NLP）领域有着广泛的应用。以下从多个方面详细介绍它：
    # 1. 核心功能
    # 生成文本嵌入：能够将句子、段落甚至文档转换为固定长度的向量表示（嵌入）。这些嵌入向量捕捉了文本的语义信息，使得语义相近的文本在向量空间中距离较近。例如，“苹果公司推出了新产品” 和 “Apple 发布了新的产品” 这两句话的嵌入向量在向量空间中会比较接近。
    # 支持多种预训练模型：提供了丰富的预训练模型，涵盖了不同语言、不同任务的需求。像 all-MiniLM-L6-v2、all-MiniLM-L12-v2 等模型在英文文本处理上表现出色，而 paraphrase-multilingual-MiniLM-L12-v2 则支持多种语言。
    vectorstore_cls=FAISS,
    # 官网地址:  https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2
    k=5,
)
print(selector)
finalT = FewShotPromptTemplate(
    example_prompt=PromptTemplate.from_template("我输入了{i}输出一个{o}"),
    example_selector=selector,
    prefix = "我给你下面的例子,你帮我推理",
    suffix = "我现在输入了{input},那么阁下又该如何应对呢?"
)
msg = finalT.format(input="那我 问你")
print(msg)
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(msg)
print(res.content)