#with_structured_output()方法,在 llm.with_structured_output()时,把会返回特殊格式
#传入Pydantic 返回 Pydantic,如果想要json,再调用model_dump_json()

#模式可以指定为 TypedDict 类、JSON Schema 或 Pydantic 类。
# 如果使用 TypedDict 或 JSON Schema，则可运行对象将返回一个字典；
# 如果使用 Pydantic 类，则将返回一个 Pydantic 对象。
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from pydantic import BaseModel, Field, model_validator, field_validator
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    # stop = "好",
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)


# 定义一个名为Joke的数据模型
# 必须要包含的数据字段：铺垫(setup)、抖包袱(punchline)
class JoJo(BaseModel):
    name: str = Field(description="jojo的奇妙冒险中的一个人物名字")
    age: int = Field(description="年龄")

    @field_validator("age")
    def age_fun(cls,value):
        if value < 18:
            print("未成年人不允许装13")
            # raise ValueError("未成年人不允许装13")
        if value >65:
            print("退休了,出去抽嘎吧,或者每天打游戏")
            # raise  ValueError("退休了,可以每天回家打游戏了")
        return value


# 实例化解析器、提示词模板
parser = PydanticOutputParser(pydantic_object=JoJo)
# 注意，提示词模板中需要部分格式化解析器的格式要求format_instructions
print("parser.get_format_instructions()=",parser.get_format_instructions())

#get_format_instructions()这个方法会返回一个字符串,如下:
# parser.get_format_instructions()= The output should be formatted as a JSON instance that conforms to the JSON schema below.
#
# As an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}
# the object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.
#Here is the output schema: #下面是输出架构
#下面是从自己写的class JoJo里面的2个字段里面添加说明里,给大模型看
# {"properties": {"name": {"description": "jojo的奇妙冒险中的一个人物名字", "title": "Name", "type": "string"}, "age": {"description": "年龄", "title": "Age", "type": "integer"}}, "required": ["name", "age"]}
t1 = ChatPromptTemplate.from_template("给我返回{count}个名字{get_format_instructions}")
prompt = t1.partial(get_format_instructions = parser.get_format_instructions())

msg = prompt.format(count = 2)
print("msg=",msg)
chain = prompt | llm
ai_msg = chain.invoke({"count":2}) #直接让llm使用invoke的话,返回的格式不能直接是json
print("ai_msg=",ai_msg)

