# JsonOutputParser 和 PydanticOutputParser (xml解析器,
# 都是通过在提示词中增加get_format_introduce 对大模型进行说明,前提是要大模型支持Json格式
# 使用的时候 prompt  | llm | parser 联合使用
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
import json

class ZhouZhou(BaseModel):
    """JoJo的奇妙冒险的对象"""#"""doc string"""
    name: str = Field(description="姓名")
    age: int = Field(description="姓名")
class ZhouZhouList(BaseModel):
    list1:list[ZhouZhou] = Field(description="ZhouZhou对象的List列表")
parser = JsonOutputParser(pydantic_object=ZhouZhouList)
# print("parser.get_format_instructions()=",parser.get_format_instructions())
prompt = ChatPromptTemplate.from_template("给我2个名字要中文{format}").partial(format = parser.get_format_instructions())
# print(prompt)
# print(prompt.format())
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
#
# chain = prompt| llm | StrOutputParser()
# # result = prompt.stream({})#chain可以stream的前提是 链里面所有的对象都能stream走通
# # for item in result:
# #     print("item=",item)
#
# ai_msg = chain.stream({})#返回json解构的字典
# for chunk in ai_msg:
#     print(chunk,end="") #这个是用字符串输出分析器的

#
chain = prompt| llm | JsonOutputParser()
ai_msg = chain.stream({})#返回json解构的字典
for chunk in ai_msg:
    jsonStr = json.dumps(chunk, ensure_ascii=False, indent=2)
    print("jsonStr",jsonStr,end="")

