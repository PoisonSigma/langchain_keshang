# 方法将示例数据转换为向量并存储在 FAISS 中，MaxMarginalRelevanceExampleSelector 利用 FAISS 进行相似性搜索，选择与输入最相关的示例。
# 解释器中安装 :  langchain-community 和 faiss-cpu 和 langchain-huggingface
# site-packages/langchain/prompts/example_selector/__init__.py
# 这个文件下有4个示例选择器from langchain.prompts.example_selector import * 会把里面的
# MaxMarginalRelevanceExampleSelector
# from sys import prefix

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.example_selectors import MaxMarginalRelevanceExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
# from langchain_openai import OpenAIEmbeddings
# from langsmith.schemas import Prompt
# from langchain.vectorstores import FAISS #已经弃用,改为如下:
from langchain_community.vectorstores import FAISS

# __all__ = [
#     "LengthBasedExampleSelector",
#     "MaxMarginalRelevanceExampleSelector",
#     "NGramOverlapExampleSelector",
#     "SemanticSimilarityExampleSelector",
# ]

# 安装依赖库：确保你已经安装了 langchain、openai、faiss-cpu 等必要的库。
# 导入所需模块：从 langchain 中导入所需的类和函数。
# 定义示例数据：准备一组示例，每个示例包含输入和输出。
# 创建示例模板：定义示例的模板格式。
# 初始化 MaxMarginalRelevanceExampleSelector：使用示例数据、嵌入模型和向量存储来初始化选择器。
# Max最大
# Marginal边际
# Relevance相关性
# 功能：结合了语义相似度和多样性，通过最大边际相关性（MMR）算法选择示例。它不仅会选择与输入语义相似的示例，还会尽量保证所选示例之间的多样性。

# 定义示例数据
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
]
t1 = PromptTemplate.from_template("输入{i}输出{o}")
s1 = MaxMarginalRelevanceExampleSelector.from_examples(
    examples,
    HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),  # 这个不需要注册,需要在解释器中安装包:langchain-huggingface
    # 官网地址:https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
    # 这个在 Hugging Face 模型中心（https://huggingface.co/models）搜索适合你任务的模型。常见的模型有：
    # all-MiniLM-L12-v2：相较于 all-MiniLM-L6-v2 层数更多，性能可能更好，但推理速度可能会稍慢。
    # OpenAIEmbeddings(),#是要使用OPenAI的API key,需要自己注册,并且产生费用
    # 在使用 langchain 进行示例选择等任务时，HuggingFaceEmbeddings 可以作为 OpenAIEmbeddings 的替代方案，它允许你在不依赖 OpenAI API 的情况下生成文本嵌入。
    # HuggingFaceEmbeddings 是 langchain 库中的一个类，用于将文本转换为向量表示（即嵌入向量），它基于 Hugging Face 的 sentence-transformers 库来实现。借助这个类，你能够使用 Hugging Face 模型中心的众多预训练语言模型，把文本数据转换为数值向量，这些向量可以用于语义搜索、文本相似度计算等自然语言处理任务。
    # 在使用 langchain 进行示例选择等任务时，HuggingFaceEmbeddings 可以作为 OpenAIEmbeddings 的替代方案，它允许你在不依赖 OpenAI API 的情况下生成文本嵌入。

    FAISS,  # from langchain.vectorstores import FAISS
    # 这里需要安装faiss-cpu,在解释器中安装, 有时候需要打开vpn
    # 有时候第一次安装的时候一直转菊花,多等一会,
    # 然后退出去,重新按的时候,会显示版本号,这时候,再安装,就可以了
    # 安装 langchain-community
    k=4,
)
# FAISS（Facebook AI Similarity Search）是由 Facebook AI Research 开发的一个用于高效相似性搜索和密集向量聚类的库。它在处理大规模向量数据时具有显著优势，被广泛应用于信息检索、图像识别、自然语言处理等领域。以下从多个方面详细介绍 FAISS：
# 主要功能
# 相似性搜索：FAISS 能够在大规模向量数据集中快速找到与给定查询向量最相似的向量。在图像检索系统中，可将图像转换为向量表示，使用 FAISS 快速找出与查询图像最相似的图像。
# 向量聚类：可以将大量向量分组到不同的簇中，使得同一簇内的向量相似度较高，不同簇之间的向量相似度较低。这在数据分析和机器学习中可用于发现数据的内在结构。
print(s1)
fspt = FewShotPromptTemplate(
    example_selector=s1,
    example_prompt=t1,
    prefix="按照下面推理的例子进行分析",
    suffix="输入{i}你应该输出什么"
)
msg = fspt.format(i="茄子")
print(msg)

# examples: List of examples to use in the prompt.用于提示的示例列表。
#


#             embeddings: An initialized embedding API interface, e.g. OpenAIEmbeddings().
# 嵌入：已初始化的嵌入 API 接口，例如 OpenAIEmbeddings ()。
# 向量存储类：一个向量存储数据库接口类，例如 FAISS。
#             vectorstore_cls: A vector store DB interface class, e.g. FAISS.
#             k: Number of examples to select. Default is 4.
# k：要选择的示例数量。默认值为 4。

# 把数据 “存入成向量”，实际上是借助数学手段，把非结构化的数据（像文本、图像、语音这类）转化成数值向量（也就是由数字构成的数组）。这一过程在人工智能领域，特别是自然语言处理（NLP）和机器学习里极为关键。下面从三个方面来详细阐释：
# 1. 数据转换的内在逻辑
# 结构化处理需求：机器学习模型没办法直接对文本、图像这类原始数据进行处理，必须把它们转化为数值形式。就拿文本来说，像 “猫” 和 “狗” 这样的词语，得通过嵌入技术（例如 HuggingFaceEmbeddings）转变为向量，这样模型才能识别出它们之间的语义联系。
# 语义的量化体现：向量中的每个数字都代表着一种语义特征。比如，在高维空间中，“苹果” 和 “香蕉” 的向量距离比较近，这就表明它们在语义上是相似的；而 “苹果” 和 “汽车” 的向量距离较远，意味着它们的相关性较低。


# 向量的维度可以任意扩展
# 二维向量：确实可以用 (x, y) 表示，例如坐标点 (3, 5)。
# 三维向量：如 (x, y, z)，可表示空间中的点。
# 高维向量：在机器学习和自然语言处理中，向量的维度通常是几十、几百甚至上千维。例如：
# all-MiniLM-L6-v2 模型生成的嵌入向量是 384 维。
# GPT 模型的向量维度可达 4096 维。
# 2. 向量的意义在于语义表示
# 在自然语言处理（如 HuggingFaceEmbeddings）拥抱 人脸嵌入中：
# 每个维度代表一种抽象语义特征，而非物理坐标。
# 高维空间能更精确地捕捉语义关系。例如：
# “猫” 和 “狗” 的向量在高维空间中距离较近。
# “银行”（金融机构）和 “银行”（河岸）的向量在特定维度上会表现出明显差异。
# 3. 二维坐标与高维向量的对比
# 特征	二维坐标	高维向量（如文本嵌入）
# 物理意义	平面上的位置	无物理意义，纯抽象语义表示
# 维度数量	2	通常 ≥ 100
# 相似性判断	计算欧氏距离（直线距离）	计算余弦相似度（方向一致性）
# 应用场景	地图定位、几何计算	语义搜索、推荐系统、情感分析等
# 总结
# 二维坐标是向量的子集，但向量的概念远不止于此。
# 在 AI 领域，向量的核心作用是将复杂信息（如语言、图像）转化为机器可处理的数值形式，高维向量能更精准地表达语义细节。
