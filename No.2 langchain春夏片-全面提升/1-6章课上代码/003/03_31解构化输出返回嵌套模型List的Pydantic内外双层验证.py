#with_structured_output()方法,在 llm.with_structured_output()时,把会返回特殊格式
#传入Pydantic 返回 Pydantic,如果想要json,再调用model_dump_json()
#模式可以指定为 TypedDict 类、JSON Schema 或 Pydantic 类。
# 如果使用 TypedDict 或 JSON Schema，则可运行对象将返回一个字典；
# 如果使用 Pydantic 类，则将返回一个 Pydantic 对象。
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field, field_validator
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")

class ZhouZhou(BaseModel):
    name: str = Field(description="jojo的奇妙冒险中的一个人物名字")
    age:int = Field(default=18)

    @field_validator('age')
    def validate_age(cls, value):
        if value < 24:
            print("内层判断--未满24岁")
            # raise ValueError("西格玛男人,从不落入女人陷阱")
        if value > 65:
            print("内层判断--退休了,可以回家打游戏,到大街上,抽嘎了")
        return value
class ZhouZhouList(BaseModel):
    list1:list[ZhouZhou] = Field(description="ZhouZhou对象的List")
    #在外层进行验证
    @field_validator('list1')
    def validate_age(cls, value):
        for obj in value:
            if obj.age < 24:
                print("未满24岁")
                # raise ValueError("西格玛男人,从不落入女人陷阱")
            if obj.age > 65:
                print("退休了,可以回家打游戏,到大街上,抽嘎了")
        return value

llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
prompt = ChatPromptTemplate.from_template("给我{count}个名字")
stru_llm = llm.with_structured_output(ZhouZhouList)#传入了Pydantic的子类,
# invoke返回就是这个类型,不能是List多个,
# 因为我们的ZhouZhou就只有2个字段
chain = prompt | stru_llm
# abcd,c,c,c,abcd,c,c,c
ai_msg = chain.invoke({"count":2})
print("ai_msg=",ai_msg)
print("type(ai_msg)=",type(ai_msg))
json = ai_msg.model_dump_json()#孩怕拼错,这个是模型转json
print("json",json)
for obj in ai_msg.list1:
    print("obj=",obj)
    ZhouZhou(name=obj.name, age=obj.age)#强行创建一个对象,进行内层的判断