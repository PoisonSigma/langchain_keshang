from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

# JsonOutputParser 和 PydanticOutputParser (xml解析器,
# 都是通过在提示词中增加get_format_introduce 对大模型进行说明,前提是要大模型支持Json格式
# 使用的时候 prompt  | llm | parser 联合使用

class ZhouZhou(BaseModel):
    "JoJo的奇妙冒险中人物的模型"
    name:str = Field(description="名字")
    age:int = Field(description="年龄")
class ZhouZhouList(BaseModel):
    list1:list[ZhouZhou] = Field(description="ZhouZhou对象的列表List")

parser = JsonOutputParser(pydantic_object=ZhouZhouList)

#这里不要单独像之前那样单独使用parsed进行验证,而是直接放到链中
prompt = ChatPromptTemplate.from_template("给我2个JoJo奇妙冒险中的人物{format}").partial(format=parser.get_format_instructions())
print("prompt.format()=",prompt.format())#打印json解析器里面给出的格式说明:
# As an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}
# the object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.
#
# Here is the output schema:
# ```
# {"$defs": {"ZhouZhou": {"description": "JoJo的奇妙冒险中人物的模型", "properties": {"name": {"description": "名字", "title": "Name", "type": "string"}, "age": {"description": "年龄", "title": "Age", "type": "integer"}}, "required": ["name", "age"], "title": "ZhouZhou", "type": "object"}}, "properties": {"list1": {"description": "ZhouZhou对象的列表List", "items": {"$ref": "#/$defs/ZhouZhou"}, "title": "List1", "type": "array"}}, "required": ["list1"]}
# ```
# parser.invoke()#他可以直接使用invoke
# parser.stream()#也可以使用stream
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
chain = prompt | llm | parser
ai_msg = chain.invoke({})
print("ai_msg=",ai_msg)
print("type(ai_msg)=",type(ai_msg))
import json
jsonStr = json.dumps(ai_msg, ensure_ascii=False, indent=2)
print("jsonStr",jsonStr)