from typing import Union

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
class ZhouZhou(BaseModel):
    name: str = Field(description="jojo的奇妙冒险中的一个人物名字")
    speed: str = Field(description="人物面板属性的速度,从ABCDE中选一个")
    strength: str = Field(description="人物面板属性的力量,从ABCDE中选一个")

class ZhouZhouList(BaseModel):
    list1:list[ZhouZhou] = Field(description="List列表,里面装的元素是ZhouZhou对象,他是JoJo的奇妙冒险中的人物名字列表")

class YiQuanChaoXiongXyy(BaseModel):
    """一拳超人中的人物"""
    name: str = Field(description="一拳超人中的人物名字")
    level: str = Field(description="评分等级,从SABC中选一个评定等级")


class YiQuanChaoXiongXyyList(BaseModel):
    list1: list[YiQuanChaoXiongXyy] = Field(description="一拳超人中人物的列表List")

class FinalResponse(BaseModel):
    dashuaige:Union[ZhouZhouList, YiQuanChaoXiongXyyList]

import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
structured_llm = llm.with_structured_output(FinalResponse)
prompt = ChatPromptTemplate.from_template("给我4个{cartoon}中的名字")
# ai_msg = (prompt | structured_llm).invoke({"cartoon":"一拳超人"})
ai_msg = (prompt | structured_llm).invoke({"cartoon":"一拳超人和jojo的奇妙冒险"})#只能选择其中一个模型
print("ai_msg=",ai_msg)
print("type(ai_msg)=",type(ai_msg))
for item in ai_msg.dashuaige.list1:
    print("item=",item)
    print("type(item)=", type(item))

print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+27----------)三(--> ")
jsonStr =  ai_msg.model_dump_json()
print("jsonStr=",jsonStr)



