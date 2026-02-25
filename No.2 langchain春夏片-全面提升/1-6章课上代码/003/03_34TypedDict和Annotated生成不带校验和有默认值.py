# 如果使用 TypedDict  将返回一个字典
# Annotated带注释的
from langchain_core.prompts import ChatPromptTemplate
from typing_extensions import Annotated, TypedDict, Optional
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
# 可以有默认值,不带校验,语法,需要让class继承自TypedDict,里面每个类属性是Annotated类型
# a:Optional[int] = "ab"
# print(a)
# print(type(a))#动态类型是运行后的真实的字符串
# a:Optional[int] = None
# print(a)
# print(type(a))#动态类型是运行后的None

class ZhouZhou(TypedDict):
    name : Annotated[str,"肘肘","JoJo的奇妙冒险中的人物名字"]#第一个是类型,第二个是默认值,第三个是给大模型的说明
    age:Annotated[int,"年龄"]
    strength:Annotated[str,"JoJo的奇妙冒险中的人物面板属性从ABCDE中选一个"]
    stamina: Annotated[Optional[str], None, "人物面板属性的持久力,从ABCDE中选一个"]
    precision: Annotated[Optional[str], None, "人物面板属性的精密性,从ABCDE中选一个"]
    growth: Annotated[Optional[str], None, "人物面板属性的成长性,从ABCDE中选一个"]
    range: Annotated[Optional[str], "E", "人物面板属性的攻击距离,从ABCDE中选一个"]
class ZhouZhouList(TypedDict):
    list1 :Annotated[list[ZhouZhou],"一个列表List里面的元素类型是ZhouZhou"]
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
model=os.getenv("MODEL_NAME"),
temperature=0.8)
stru_llm = llm.with_structured_output(ZhouZhouList)
prompt =ChatPromptTemplate.from_template("给我2个名字")
ai_msg = (prompt | stru_llm).invoke({})#提示词模板的invoke的input参数不能为空,所以要给一个键值对为空的字典{}dict
print("ai_msg=",ai_msg)
print("type(ai_msg)=",type(ai_msg))
import json
jsonStr = json.dumps(ai_msg, ensure_ascii=False, indent=2)
print("jsonStr=",jsonStr)
