#注意本课要开启vpn,否则运行报错:(MaxRetryError("HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json (Caused by ConnectTimeoutError(<HTTPSConnection(host='huggingface.co', port=443) at 0x12f19d550>, 'Connection to huggingface.co timed out. (connect timeout=10)'))"), '(Request ID: 3aa7dc85-60c9-4c09-ac0f-1ad098ebf228)')' thrown while requesting HEAD https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/./modules.json


# 解释器中安装 :  langchain-community 和 faiss-cpu 和 langchain-huggingface
# MaxMarginalRelevanceExampleSelector最大边际相关性示例选择器
# 最大边际相关性（MMR）算法
# 相关性（Relevance）
# 首先通过向量嵌入（如OpenAI的文本嵌入模型）计算输入问题与示例库中所有示例的相似度，筛选出最相关的候选集。
# 多样性（Diversity）
# 在候选集中，逐步选择与已选示例差异最大的新示例。通过调整参数 lambda 控制二者的权重：


#本课需要安装uv add faiss-cpu, 不指定版本,让uv自己适配版本,否则运行不了
import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.example_selectors import MaxMarginalRelevanceExampleSelector
from langchain_community.vectorstores import FAISS

from langchain_openai import ChatOpenAI

# 设置环境变量，禁用 tokenizers 分词器 并行处理
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
# TOKENIZERS_PARALLELISM 是 Hugging Face 的 tokenizers 库中的一个环境变量，用于控制分词过程中是否启用多线程并行处理。它的作用和相关背景如下：
# 核心作用
# 并行加速
# 当设置为 true（默认值）时，分词器会利用多线程并行处理文本，显著提升处理速度，尤其适用于长文本或大规模数据集。
# 例如，处理一个包含数千条句子的数据集时，并行分词能节省大量时间。
# 避免死锁
# 如果代码在 fork（创建子进程）之后使用 tokenizers 库，可能导致资源竞争或死锁（如子进程重复初始化线程池）。此时，库会自动禁用并行处理并发出警告。
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
# Max最大
# Marginal边际
# Relevance相关性
# 功能：结合了语义相似度和多样性，通过最大边际相关性（MMR）算法选择示例。它不仅会选择与输入语义相似的示例，还会尽量保证所选示例之间的多样性。
s1 = MaxMarginalRelevanceExampleSelector.from_examples(
    examples,
    HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
    # OpenAIEmbeddings(),#是要使用OPenAI的API key,需要自己注册,并且产生费用
    # 在使用 langchain 进行示例选择等任务时，HuggingFaceEmbeddings 可以作为 OpenAIEmbeddings 的替代方案，它允许你在不依赖 OpenAI API 的情况下生成文本嵌入。
    # 这个不需要注册,需要在解释器中安装包:langchain-huggingface
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
    k=6  # 选取出多少个示例
)
print(s1)
t1 = PromptTemplate.from_template("输入了{i}输出一个{o}")
fspt = FewShotPromptTemplate(
    example_selector=s1,
    example_prompt=t1,
    prefix="我输入下面的例子,你来推理吧",
    suffix="我现在输入一个{i},你推理一下,输出什么?"
)
msg = fspt.format(i="蛋清屁")
print(msg)
# 功能：结合了语义相似度和多样性，通过最大边际相关性（MMR）算法选择示例。它不仅会选择与输入语义相似的示例，还会尽量保证所选示例之间的多样性。
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
# print(msg)
res = llm.invoke(msg)
# print(res.content)
