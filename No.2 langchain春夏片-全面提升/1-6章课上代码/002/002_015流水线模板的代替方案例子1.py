# PipelinePromptTemplate
# 第1个提示词里面有一些占位符,比如叫name
# 第2个提示词里面有一些占位符,比如叫age
# 第3个提示词里面有一些占位符,比如叫gender
#最终要的提示词模板是,包括上面3个提示词模板的 所有占位符
#那么最终的提示词模板就要包含前面所有提示词模板的占位符 ,name ,age ,gender
from langchain_core.prompts import PromptTemplate

t1 = PromptTemplate.from_template("我自我介绍一下,我的姓名是:{name}")
t2 = PromptTemplate.from_template("我要自我介绍了:{introduce}")
t3 = PromptTemplate.from_template("开始吟唱:{words}")
#嵌套关系的例子
finalT = PromptTemplate.from_template("""
                             {p1}
                             {p2}
                             {p3}
                             """)
p1 = t1.format(name = "肘肘")
p2 = t2.format(introduce = "你影响我睡觉了,我要开始报复性逃班了")
p3 = t3.format(words = "无挖一挖木~新的一路")
msg = finalT.format(p1 = p1 ,p2 = p2 ,p3 = p3)
print(msg)
# 无挖一挖木~新的一路

