# 使用OutputFixingParser进行错误修复 输出修复解析器
from langchain_classic.output_parsers import OutputFixingParser
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel,Field


class ZhouZhou(BaseModel):
    name: str = Field(description="姓名")
    age: str = Field(description="年龄")
parser = PydanticOutputParser(pydantic_object=ZhouZhou)
# prompt = ChatPromptTemplate.from_template("给我一个名字{format_instructions}").partial(format_instructions=parser.get_format_instructions())
# str2 = prompt.format()
# print("str2=",str2)
# print("prompt=",prompt)

import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    # stop = "三",#这里可以有stop参数的时候,下面的bind()方法,才可以绑定参数
     temperature=0.8)
#print((prompt | llm).invoke({}).content) #证明返回的是一个json结构的结果
bad_response = '{"name":"李四"}'#模拟一个坏的返回的输出,要字符串的json
# bad_response = '{"name":"张三","age":"30"}'#模拟正常结果,不会被try捕获
#下面是用try来证明解析器会出错
try:
    resultNormal =parser.invoke(bad_response)#尝试运行,如果这里运行出错,就会在下面except捕获到,而不会崩
    print("resultNormal=",resultNormal)
except OutputParserException as e:# 这个是把捕获到的异常保存到e当中
    print("e=",e)
    # 错误以后给输出修复解析器传入新的llm和解析器
    # llm2 = llm.bind(stop="三")
    llm2 = llm.bind(stop="0")#给Rannable对象绑定一个参数
    try:
        #这里是又发了一次请求
        fixingParser = OutputFixingParser.from_llm(llm=llm2, parser=parser)#传之前的大模型和解析器
        # 把第一次请求返回的坏的请求穿进去,prompt_value是提示词format_prompt()后的结果
        # prompt_value = prompt.format_prompt()
        # #把第一次请求返回的坏的请求穿进去,prompt_value是提示词format_prompt()后的结果
        # result =fixingParser.parse_with_prompt(bad_response, prompt_value)
        # print("重新请求后的结果是:",result)
        result = fixingParser.parse(bad_response)#可以直接解析
        print("重新请求后的结果是:", result)
    except OutputParserException as e:  # 这个是把捕获到的异常保存到e当中
        print("第二个e=", e)