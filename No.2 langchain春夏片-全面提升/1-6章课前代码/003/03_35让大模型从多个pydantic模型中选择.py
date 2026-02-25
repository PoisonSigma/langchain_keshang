from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel,Field


class ZhouZhou(BaseModel):
    name:str = Field(description="JoJo的奇妙冒险中的人物名字" )
    speed:str = Field(description="人物面板属性的速度,从ABCDE中选一个" )
    strength:str = Field(description="人物面板属性的力量,从ABCDE中选一个" )

class ZhouZhouList(BaseModel):
    list1:list[ZhouZhou] = Field(description="List列表,里面装的元素是ZhouZhou对象,他是JoJo的奇妙冒险中的人物名字列表" )

class YiQuanChaoXiongXyy(BaseModel):
    """一拳超人中的人物"""
    name: str = Field(description="一拳超人中的人物名字")
    level: str = Field(description="评分等级,从SABC中选一个评定等级")


class YiQuanChaoXiongXyyList(BaseModel):
    list1: list[YiQuanChaoXiongXyy] = Field(description="一拳超人中人物的列表List")

#Union 是类型注解工具，它来自 typing 模块
#Union 可用于指明一个变量、参数或者返回值能够是多种不同类型中的任意一种。下面为你详细介绍它的用法。
from typing import Union
def add( a:Union[int,float],b:Union[int,float]): #格式Union[里面多个类型用,逗号隔开]
    result = a+b
    print("result=",result)
add(1,2.1)



class FinalResponse(BaseModel):
    #Union联合类型,代表里面可能是2种类型YiQuanChaoXiongXyyList或ZhouZhouList
    result:Union[YiQuanChaoXiongXyyList,ZhouZhouList] #需要包含文件from typing import Union

import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
prompt = ChatPromptTemplate.from_template("告诉我2个{cartoon}的名字")
stru_llm = llm.with_structured_output(FinalResponse)
ai_msg = (prompt | stru_llm).invoke({"cartoon":"一拳超人和JoJo的奇妙冒险"})#这样不行,只能选择一个模型
jsonStr = ai_msg.model_dump_json()
print("jsonStr=",jsonStr)


