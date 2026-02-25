"""
自定义模板方法:
1.继承父类 :StringPromptTemplate
调用的时候传入必传参数 input_variables,这是一个[] List,
里面的值按照要求,要跟后面调用fotmat的值一样
例如input_variables=["talk1", "talk2"])
format 也要穿talk1,talk2
虽然不这么传,语法也能过,但是约定这么写,可以让调用的人看明白
"""

import os
from typing import Any

from dotenv import load_dotenv
from langchain_core.prompts import StringPromptTemplate
from langchain_core.prompts.base import FormatOutputType
from langchain_openai import ChatOpenAI


# 之前讲过class PromptTemplate 继承自StringPromptTemplate
class PsPromptTemplate(StringPromptTemplate):
    # format是抽象方法需要自己实现
    #  FormatOutputType 与 str 的关系
    # 类型注解，类型注解的主要作用是给开发者和静态类型检查工具（像
    # mypy）提供类型提示，并不会在运行时对类型进行强制约束。下面详细解释：
    # 1.
    # 类型注解的本质
    # 类型注解只是对变量或函数返回值类型的一种声明，它不会改变代码的实际运行逻辑。在
    # Python
    # 运行时，并不会因为你给某个变量或返回值标注了
    # FormatOutputType
    # 就对其类型进行转换或者检查。
    # 在 LangChain 里，FormatOutputType 通常是一个宽泛的类型定义，它可能包含 str 类型
    def format(self, **kwargs: Any) -> FormatOutputType:
        #
        # for v in kwargs.values():  #kwargs.values()是传入参数的值,不能用k,v2个变量解包,而items,可以用2个参数解包
        #     print(v)
        # print("戟把离手越进义父离你越远>---红字增幅+25----------)三(--> ")
        # for item in kwargs.items():#item 是一个元组（tuple）类型
        #     print(item)
        # print("戟把离手越进义父离你越远>---红字增幅+25----------)三(--> ")
        # for k,v in kwargs.items():
        #     print(k)
        #     print(v)

        result: str = "吉良吉影说:" + kwargs["talk1"] + "\n" + kwargs["talk2"]
        # print(result)

        return result #result是字符串类型,但是函数返回值的类型注解是FormatOutputType


# t1 = PsPromptTemplate(input_variables=["talk1", "talk2"]).format(talk1="我想要过平静的生活",
#                                                                  talk2="你就是阻碍我睡眠的的烦恼"
#                                                                  )
#下面是自己瞎写的input_variables,但是format是自己写的所以也能组合正确
t1 = PsPromptTemplate(input_variables=["a"]).format(talk1="我想要过平静的生活",
                                                                 talk2="你就是阻碍我睡眠的的烦恼"
                                                                 )
print(t1)
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(t1)
print(res.content)
