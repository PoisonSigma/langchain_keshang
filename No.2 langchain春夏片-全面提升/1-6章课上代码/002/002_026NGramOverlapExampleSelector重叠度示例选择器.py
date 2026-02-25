# NGramOverlapExampleSelector是 LangChain 里的一种示例选择器，其作用是从给定的示例集合里，挑选出与输入文本在 N - gram 层面重叠度较高的示例。下面为你详细介绍它的相关内容：
# 核心概念
# N - gram：这是自然语言处理里的一个基础概念，指的是文本中连续的 N 个元素。这里的元素一般是词或者字符。例如，对于文本 “自然语言处理”，当 N = 2 时，其 2 - gram（即 bigram）有 “自然”“语言”“处理”。
# 示例选择器：在少样本学习中，往往有大量示例可供选择，而示例选择器的任务就是从这些示例里挑出和当前输入最相关的示例，以此提升模型的性能。

#把少量样本里面输入的词作为参考,去例子的List去找对应的例子,选择出来
# 解释器安装包这个是英文设计的分词器:  nltk
import nltk
import ssl
import jieba
# 中文分词器安装包:jieba
from langchain_community.example_selectors import NGramOverlapExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# 临时禁用 SSL 验证
# 如果已经下载了就不用下载
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download('punkt')
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
    {"i": "蛋白粉样子的生石灰", "o": "要你命三千"},
    {"i": "巧克力味的咖啡", "o": "饮料"},
    {"i": "巧克力样子的芝麻酱拌红糖", "o": "甜食"},
]
# o ma e | wa | mou | xindeiyilv
# 你 | 语气助词 | 已经 | 死了
processed_examples = []#添加空格以后得分词
#下面是自己做的中文分词,每个次之间添加空格,为了让英文分词器其效果
for example in examples:
    processed_i = " ".join(jieba.cut(example["i"]))
    processed_o = example["o"]
    processed_examples.append({"i": processed_i, "o": processed_o})
print(examples)
print(processed_examples)
t1 = PromptTemplate.from_template("输入{i}输出{o}")
s1 = NGramOverlapExampleSelector(
    examples=examples,
    example_prompt=t1,
    threshold= 0,  # 阈值 ,0是删除掉与输入词无重叠的
)
# 算法停止的阈值。默认设置为-1.0。
#
#     当阈值为负数时：
#     select_examples会按ngram_overlap_score对示例排序，但不排除任何示例。
#     当阈值大于1.0时：
#     select_examples会排除所有示例，并返回空列表。
#     当阈值等于0.0时：
#     select_examples会按ngram_overlap_score对示例排序，
#     并排除与输入没有n-gram重叠的示例。
# n-gram 重叠计算：根据输入与示例的连续 n 个词的重叠程度排序示例
# 阈值过滤：
# threshold=0.0 排除完全无重叠的示例
# threshold=0.5 仅保留重叠度≥50% 的示例
fspt = FewShotPromptTemplate(
    example_selector=s1,
    example_prompt=t1,
    prefix="我输入下面的例子,你来推理吧",
    suffix="我现在输入一个{i},你推理一下,输出什么?"
)
# msg = fspt.format(i="巧克力")
msg = fspt.format(i="蛋白粉")
print(msg)
