import json
from typing import Optional

from langchain_core.prompts import ChatPromptTemplate
from typing_extensions import Annotated, TypedDict
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
# 如果使用 TypedDict  将返回一个字典
#Annotated翻译:有注释的
# a:Optional[int] = None #可空类型
# print(a)
#
class ZhouZhou(TypedDict):
    name:Annotated[str,"JoJo的奇妙冒险里面人物的名字"]
    age:Annotated[int,"年龄"]
    speed:Annotated[str,"人物面板属性的速度,从ABCDE中选一个"]
    strength: Annotated[str, "人物面板属性的力量,从ABCDE中选一个"]
    stamina: Annotated[Optional[str],None, "人物面板属性的持久力,从ABCDE中选一个"]
    precision:Annotated[Optional[str],None, "人物面板属性的精密性,从ABCDE中选一个"]
    growth: Annotated[Optional[str], None, "人物面板属性的成长性,从ABCDE中选一个"]
    range: Annotated[Optional[str], None, "人物面板属性的攻击距离,从ABCDE中选一个"]
class ZhouZhouList(TypedDict):
    list1:Annotated[list[ZhouZhou],"List列表,里面装的元素是ZhouZhou对象"]

load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
stru_llm = llm.with_structured_output(ZhouZhouList)
prompt = ChatPromptTemplate.from_template("给我2个名字")
ai_msg = (prompt | stru_llm).invoke({})
#这里prompt的invoke里面的input是必填项,所以要用没有键值对的dict,{}填充
print("ai_msg=",ai_msg)
print("type(ai_msg)=",type(ai_msg))
jsonStr = json.dumps(ai_msg, ensure_ascii=False, indent=2)
print("jsonStr=",jsonStr)
#
