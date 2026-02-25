#定义一个 BaseModel的子类,作用是定义一个可以被大模型识别的语言描述
#也可以继承 TypedDict 类,但是我们掌握一个BaseModel就好了,后面再用@tool
#意义,例如:数学类的,如果大模型处理例如数学运算等,比较麻烦,我们就给他传一个 自定义的函数,让他进行运算
#给大模型传很多工具,他可以"auto",是可以让大模型自动帮我们选择用那个tool,或者是自己强制指定那个工具
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from sympy.strategies.core import switch


#tool 翻译过来时工具的意思,但实际用的时候,他是要最终调用自定义的函数,
# 也可以不调用,最终取决于程序员自己
class add(BaseModel):#这个类是给大模型看的
    """加法运算,让2个数字相加"""#这里是说明tool的doc string文档字符串,不写不报错,但是大模型无法参考是否选择这个工具
    a:int = Field(description="第1个数字")#这个描述信息,是给大模型看的
    b:int = Field(description="第2个数字")#这个描述信息,是给大模型看的


class whichBigger(BaseModel):
    """哪个数字大"""#这里是说明tool的doc string文档字符串,不写会报错:invalid  doc string 无效的文档字符串
    c:int = Field(description="第1个数字")#这个描述信息,是给大模型看的
    d:int = Field(description="第2个数字")#这个描述信息,是给大模型看的

#定义自己要调用的函数
def add_function(a,b):
    result = a+b
    print("调用了add_function(),结果是", result)
    return result


def whichBigger_function(c,d):#故意起名不一样的参数
    print("调用了whichBigger_function()")
    if (c>d):
        print(c,"大")
    else:
        print(d, "大")

tools = [add,whichBigger]#把定义好的工具的类放到列表里面
print(type(tools))


load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    # model="deepseek-reasoner",#推理模型不支持函数调用
    temperature=0.8)
llm_with_tools = llm.bind_tools(tools)#将工具列表绑定到 llm 实例上，得到一个新的实例
print(type(llm_with_tools))
msg = "1+2=多少? 9.8和9.12哪个大?"#可以提出多个问题,让大模型选择多个工具
ai_msg = llm_with_tools.invoke(msg)#实际上返回的是AiMessage
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print("ai_msg",ai_msg)
#每个tool_calls 每个都有一个id,用来标明唯一标识符的,例如异步,操作的时候可以标明是否是同一个tool
print("type(ai_msg)",type(ai_msg))
print("ai_msg.tool_calls",ai_msg.tool_calls)#拿到llm帮我们选择的tool
# dic1 = {"name":"佛山黄飞鸿"}
# print(dic1["name"])
print({"name": "佛山黄飞鸿"}["name"])
for tool in ai_msg.tool_calls:
    # {"add":"发现add","whichBigger":"发现whichBigger"}["add"]
    # print({"add":"发现add","whichBigger":"发现whichBigger"}["add"])
    # print(tool["name"])
    # str1 = {"add": "发现add", "whichBigger": "发现whichBigger"}[tool["name"]]
    # print(str1)
    args = tool["args"]#获取参数的字典
    print(args)
    # #下面是获取每次遍历的函数
    print("tool名,传入的class名:",tool["name"] )
    #下面错误的原因是,for in 循环的时候,左边字典部分,的 a,b, c,d 不是每次遍历都能取到args["a"],args["b"],args["c"],args["d"],
    # {"add": add_function(args["a"],args["b"]), "whichBigger": whichBigger_function(args["a"],args["b"])}[tool["name"]]
    # fun = {"add": add_function, "whichBigger":whichBigger_function}[tool["name"]]
    # # #根据不同的函数传入不同的参数
    # if fun == add_function:
    #     add_function(args["a"], args["b"])
    # if fun == whichBigger_function:
    #     whichBigger_function(args["c"], args["d"])
    # print("tool名,传入的class名:",tool["name"] )
    if tool["name"] == "add":
        add_function(args["a"], args["b"])
    if tool["name"] == "whichBigger":
        whichBigger_function(args["c"], args["d"])