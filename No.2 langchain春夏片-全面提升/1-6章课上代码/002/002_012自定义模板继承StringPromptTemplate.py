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


# shit mountain king
# the king of shit mountain
class PsPromptTemplate(StringPromptTemplate):
    def format(self, **kwargs: Any) -> FormatOutputType:
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
        # result:str = "吉良吉影说:" +kwargs ["talk1"] + "\n"+ kwargs ["talk2"]
        # result: str = "吉良吉影说:" + kwargs["talk1"] + "\n" + kwargs["talk2"]
        result: str = "吉良吉影说:"
        for v in kwargs.values():
            result+= v + "\n"
        return result
# msg = PsPromptTemplate(input_variables = ["talk1","talk2"]).format(talk1= "我想要过平静的生活",talk2="你就是阻碍我睡眠的的烦恼")
# print(msg)
# print(type(msg)) #打印运行时类型
# print(type(123))
msg = PsPromptTemplate(input_variables = [""]).format(talk1= "我想要过平静的生活",talk2="你就是阻碍我睡眠的的烦恼",talk3="请问我自行车没气了你能给我修吗?")
print(msg)
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(msg)
print(res.content)
"""
吉良吉影是《JOJO的奇妙冒险》中的角色，这是一个动漫虚构情境下的趣味问答。
从现实角度来说，我没有实体也无法直接修理自行车。但如果是在动漫设定那种奇幻情境下，以吉良吉影追求平静生活又有些“不讲道理”的风格，他可能会拒绝帮忙修自行车，毕竟他只想要没有干扰自己平静生活的状态，修自行车这种麻烦事可能不在他的考虑范围内，不过这只是基于角色性格的一种趣味推测啦。
"""