from langchain_core.output_parsers import PydanticOutputParser
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

parser = PydanticOutputParser(pydantic_object=ZhouZhouList)

#这里不要单独像之前那样单独使用parsed进行验证,而是直接放到链中
prompt = ChatPromptTemplate.from_template("给我2个JoJo奇妙冒险中的人物{format}").partial(format=parser.get_format_instructions())
print("prompt.format()=",prompt.format())

import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
chain = prompt | llm | parser
ai_msg = chain.stream({})
for item in ai_msg:
    # print(item)
    jsonStr = item.model_dump_json()
    print(jsonStr)