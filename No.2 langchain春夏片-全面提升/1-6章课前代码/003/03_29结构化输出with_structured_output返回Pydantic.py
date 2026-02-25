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
prompt = ChatPromptTemplate.from_template("给我返回{count}个名字")

#
# # 使用LCEL语法组合一个简单的链
# print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")


# ai_msg = chain.invoke({"count":2}) #直接让llm使用invoke的话,返回的格式不能直接是json
# print("ai_msg=",ai_msg)
# parser.invoke(ai_msg)#这里返回的不是json,不能直接用解析器

stru_llm =   llm.with_structured_output(JoJo) #让大模型进行结构化输出
# print("stru_llm=",stru_llm)
# print("type(stru_llm)=",type(stru_llm))#类型是RunnableSequence
# prompt_msg = prompt.invoke({"count":2})
# print("prompt_msg=",prompt_msg)
# result = stru_llm.invoke(prompt_msg)#注意,这个结果是JoJo类型的对象是pydantic类型,这个类再被创建对象的时候进行验证
# print("result=",result)
# print("type(result)=",type(result))

#
chain = prompt | stru_llm
ai_msg = chain.invoke({"count":2})#这里with_structured_output传入的是Pydantic,返回也是
print("ai_msg=\n",ai_msg)
json = ai_msg.model_dump_json()
print("json=\n",json)
