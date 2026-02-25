# 简化重试的过程,可以放在复杂的链中的一部分,整合了之前解析器,大模型,之前返回的提示词,坏的错误输出,
# 整合了后面4个 ,prompt | llm | parser | bad_response
from langchain.output_parsers import RetryOutputParser
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class ZhouZhou(BaseModel):
    name: str = Field(description="姓名")
    age: str = Field(description="年龄")


parser = PydanticOutputParser(pydantic_object=ZhouZhou)
prompt = ChatPromptTemplate.from_template("给我一个名字{format_instructions}").partial(
    format_instructions=parser.get_format_instructions())
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
# print((prompt | llm).invoke({}).content) #证明返回的是一个json结构的结果
bad_response = '{"name":"张三"}'  # 模拟一个坏的返回的输出,要字符串的json
# 下面是用try来证明解析器会出错
try:
    parser.invoke(bad_response)  # 尝试运行,如果这里运行出错,就会在下面except捕获到,而不会崩
except OutputParserException as e:  # 这个是把捕获到的异常保存到e当中
    print("e=", e)
    # 这里发现异常以后,就执行重试输出解释器
    retryParser = RetryOutputParser.from_llm(llm=llm, parser=parser)
    prompt_value = prompt.format_prompt()
    result = retryParser.parse_with_prompt(bad_response, prompt_value)

    print("重新解析的结果:", result)




