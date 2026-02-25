#with_structured_output()方法,在 llm.with_structured_output()时,把会返回特殊格式
#传入Pydantic 返回 Pydantic,如果想要json,再调用model_dump_json()
#模式可以指定为 TypedDict 类、JSON Schema 或 Pydantic 类。
# 如果使用 TypedDict 或 JSON Schema，则可运行对象将返回一个字典；
# 如果使用 Pydantic 类，则将返回一个 Pydantic 对象。
from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
#模式可以指定为 TypedDict 类、JSON Schema 或 Pydantic 类。
# 如果使用 TypedDict 或 JSON Schema，则可运行对象将返回一个字典；
# 如果使用 Pydantic 类，则将返回一个 Pydantic 对象。
#一次看个痛

from pydantic import BaseModel, Field, field_validator
class ZhouZhou(BaseModel):
    name: str = Field(description="JoJo的奇妙冒险里的人物名字")
    age:int = Field(default=18)
    @field_validator('age')
    def validate_age(cls,value):
        if value < 18:
            print("未满十八岁")
            # raise ValueError("西格玛男人,从不落入女人陷阱")
        if value > 65:
            print("退休了,可以回家打游戏,到大街上,抽嘎了")
        return value

class ZhouZhouList(BaseModel):
    list1:list[ZhouZhou] = Field(description="ZhouZhou对象的List")

prompt = ChatPromptTemplate.from_template("给我{count}个名字")#大模型直呼:王总好~


load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
model=os.getenv("MODEL_NAME"),
 temperature=0.8)
# chain = prompt | llm
# ai_msg = chain.invoke({"count":2})#不是输出的json
# print(ai_msg)

stru_llm = llm.with_structured_output(ZhouZhouList)#传入Pydantic子类,以后再invoke就能返回Pydantic子类对象
chain = prompt | stru_llm
ai_msg = chain.invoke({"count":2})
print(ai_msg)
json = ai_msg.model_dump_json()
for obj in  ai_msg.list1:
    print("obj=",obj)

