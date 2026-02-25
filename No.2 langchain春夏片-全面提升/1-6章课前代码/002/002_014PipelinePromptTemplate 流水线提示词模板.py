#Pipeline流水线的意思
#PipelinePromptTemplate 流水线提示词模板作用,把多个模板组合到一起,完成复杂的最终提示词
# PipelinePromptTemplate允许将整个提示构建过程拆分成多个步骤，每个步骤使用一个独立的提示模板来处理特定的信息，最后组合成完整的提示。

#例如下面场景:jojo中的吉良吉影的名场面会完成一大段的行为,简单分为3部曲
#1.打招呼
#2.自我介绍
#3.你影响我睡觉了
#把上面3个行为分成3个提示词模板,组成最终的提示词模板

#cmd+F12查看类结构图
# m代表方法method
#f代表field字段属性,变量的意思

#找到里面的2个属性:
# final_prompt: BasePromptTemplate
#     """The final prompt that is returned."""
#     pipeline_prompts: list[tuple[str, BasePromptTemplate]]
#     """A list of tuples, consisting of a string (`name`) and a Prompt Template."""

# pipeline_prompts 是一个列表，列表中的每个元素是一个元组。每个元组包含两个部分，
# 第一个部分是一个字符串，表示该提示模板的输出变量名；
# 第二个部分是一个 PromptTemplate 实例，即一个具体的提示模板。
# 作用：它定义了一系列按顺序执行的提示模板，这些模板会依次处理输入数据，
# 每个模板的输出会作为下一个模板的输入。这样可以将复杂的提示生成过程拆分成多个简单的步骤
# ，每个步骤负责完成特定的任务。
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain_core.prompts import PromptTemplate

# 第一个提示模板，用于生成电影的类型
#input_variables 里面的字符串,要跟后面模板中占位的字符串相同,为了让开发人员能知道哪些字符串是用来占位的
t1 = PromptTemplate(
    # input_variables=["abc"], #这里写不写都行
    template="请推荐一个{genre}类型的电影名字: "
)

t1b = PromptTemplate.from_template("请推荐一个{genre}类型的电影名字: ")
#from_template会把里面占位的{}里面的变量自动输入到input_variables里面
print(type(t1))
print(type(t1b))
print(t1)
print(t1b)
print(t1.input_variables)
print(t1b.input_variables)
# 第二个提示模板，用于根据电影名字生成电影简介
t2 = PromptTemplate(
    template="请简要描述一下电影《{movie_name}》的剧情: "
)
#下面是一个List,里面的元素类型是元组 list[tuple[str, PromptTemplate]]

pipeline_prompts2 = [
    ("movie_name", t1),
    ("movie_description", t2)
]
final_prompt2 = PromptTemplate.from_template("""
{movie_name}
{movie_description}
                                            """)
# fp = PipelinePromptTemplate(pipeline_prompts=pipeline_prompts2,final_prompt=final_prompt2)
# # 提供最开始的输入变量
# input_dict = {"genre": "科幻"}

from langchain.prompts import PromptTemplate

# 定义提示模板
t1 = PromptTemplate.from_template("请推荐一个{genre}类型的电影名字: ")
t2 = PromptTemplate.from_template("请简要描述电影《{movie_name}》的剧情: ")
final_prompt = PromptTemplate.from_template("{movie_name}\n{movie_description}")

pipeline_prompts = [
    ("movie_name", t1),
    ("movie_description", t2)
]

# 初始化输入
my_input = {"genre": "科幻"}

# 执行流水线
for name, prompt in pipeline_prompts:
    # 调用提示模板并获取结果
    result = prompt.invoke(my_input).to_string()
    # 将结果存入输入字典
    my_input[name] = result

# 执行最终提示
final_output = final_prompt.invoke(my_input)
print(final_output)
