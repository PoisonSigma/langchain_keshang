from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field, field_validator
class Zhouzhou(BaseModel):
    name: str = Field(description="JoJo的奇妙冒险里的人物名字")
    age:int = Field(default=18)
@field_validator('age')
def validate_age(value):
    if value < 18:
        print("未满十八岁")
        raise ValueError("西格玛男人,从不落入女人陷阱")
    if value > 65:
        print("退休了,可以回家打游戏,到大街上,抽嘎了")


parser = PydanticOutputParser(pydantic_object = Zhouzhou)
# result = parser.get_format_instructions()
# print("result=",result)
#get_format_instructions()这个方法会返回一个字符串,如下:
# parser.get_format_instructions()= The output should be formatted as a JSON instance that conforms to the JSON schema below.
#
# As an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}
# the object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.
#Here is the output schema: #下面是输出架构
#下面是从自己写的class zhouzhou里面的2个字段里面添加说明里,给大模型看
#{"properties": {"name": {"description": "JoJo的奇妙冒险里的人物名字", "title": "Name", "type": "string"}, "age": {"default": 18, "title": "Age", "type": "integer"}}, "required": ["name"]}

t1 = ChatPromptTemplate.from_template("给我{count}个名字{get_format_instructions}")
prompt = t1.partial(get_format_instructions= parser.get_format_instructions())
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    # stop = "好",
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
chain = prompt | llm | StrOutputParser()
ai_msg = chain.invoke({"count":2})
print(ai_msg)

