# 任何两个可运行对象可以“链式”组合成序列。
# 前一个可运行对象的 .invoke() 调用的输出作为输入传递给下一个可运行对象。
# 这可以使用管道操作符 (|) 或更明确的 .pipe() 方法来完成，二者效果相同。
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("你好,我是{city}{name}")
prompt2 = prompt.partial(city = "哈尔滨")
print("prompt2",prompt2)
msg = prompt2.invoke({"name" :"吴彦祖"})#注意提示词模板也可以invoke,需要输入一个input参数是一个字典
print("msg",msg)
prompt2.invoke({"name": "吴彦祖"})

# msg = prompt2.format(name = "吴彦祖")#但是这个只是普通字符串,不能使用管道操作符
# print("msg",msg)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
#把前一个提示词模板invoke的输出,作为第二个invoke参数
# res = llm.invoke(prompt2.invoke({"name": "吴彦祖"}) )
# print("res",res)
#等价于下面
# res = (prompt2|llm).invoke({"name": "吴彦祖"})#这里实际上只有第一次的提示词是用户输入的,提示词输入变成了llm的invoke的发送请求的参数列表输出
# print("res",res)
text = StrOutputParser().invoke((prompt2|llm).invoke({"name": "吴彦祖"}))
#上面代码推导过程: (prompt2|llm).invoke({"name": "吴彦祖"}) |   StrOutputParser()
#(prompt2 | llm | StrOutputParser()).invoke({"name": "吴彦祖"})
print("text",text)
# chain1 = prompt2 | llm
# chain1.invoke()