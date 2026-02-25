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


# from langchain_core.prompts import PipelinePromptTemplate
#
# PipelinePromptTemplate
# 第1个提示词里面有一些占位符,比如叫name
# 第2个提示词里面有一些占位符,比如叫age
# 第3个提示词里面有一些占位符,比如叫gender
#最终要的提示词模板是,包括上面3个提示词模板的 所有占位符
#那么最终的提示词模板就要包含前面所有提示词模板的占位符 ,name ,age ,gender
from langchain_core.prompts import PromptTemplate
#
# t1 = PromptTemplate.from_template("我自我介绍一下,我的姓名是:{name} {age} {gender}")
# # prompt1 = t1.format(name = "吉良吉影",age = 18,gender = "男")
# # print(prompt1)
# #from_template方法会自动给input_variables赋值
# # print("t1.input_variables = %s" % t1.input_variables )
#
# print( t1.input_variables )
# for v in t1.input_variables :
#     print(v)

p1 = PromptTemplate(
input_variables = ["gender"], #这里面不会影响后面的input_variables的结果
template =  "姓名{name} 年龄 {age}"
)
print(p1.input_variables)
