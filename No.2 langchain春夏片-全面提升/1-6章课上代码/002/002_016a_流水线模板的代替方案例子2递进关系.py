from tkinter.font import names

from langchain_core.prompts import PromptTemplate

t1 = PromptTemplate.from_template("我自我介绍一下,我的姓名是:{name}")
p1 = t1.format(name = "肘肘")
#递进关系的流水线模板的代替方案
#递进关系的例子
print("p1=",p1)
t2 = PromptTemplate.from_template("{result1} 我要自我介绍了,我叫{name}")
msg = t2.format(result1 = p1,name = "肘肘")
print(msg)
