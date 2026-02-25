# 定义示例数据
# 解释器安装包这个是英文设计的分词器:  nltk
# 中文分词器安装包:jieba
from langchain_community.example_selectors import NGramOverlapExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langsmith.schemas import Prompt
import nltk
import jieba
import ssl

# 下载必要的数据
# 临时禁用 SSL 验证
# 如果已经下载了就不用下载
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
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
t1 = PromptTemplate.from_template("输入{i}输出{o}")


processed_examples = [] #添加空格以后得分词
for example in examples:
    processed_i = " ".join(jieba.cut(example["i"]))
    processed_o = example["o"]
    processed_examples.append({"i": processed_i, "o": processed_o})
print(examples)
print(processed_examples)

s1 = NGramOverlapExampleSelector(
    # examples=examples,#中文分词不支持,使用自己添加空格之后的分词例子
examples=processed_examples,#中文分词不支持,使用自己添加空格之后的分词例子
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

# print(s1)
fstp = FewShotPromptTemplate(
    example_selector=s1,
    example_prompt=t1,
    prefix="按照下面推理的例子进行分析",
    suffix="输入{i}你应该输出什么"
)
# msg = fstp.format(i="蛋白粉")
msg = fstp.format(i="巧克力")
print(msg)
