from langchain_community.chat_models import ChatHunyuan
from langchain_core.output_parsers import XMLOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

parser = XMLOutputParser(tags=["语言风格","性格特点","穿衣风格","对待女人态度","对待打压自己人的态度","对待工作技能态度","对待比自己小的弟弟们的态度","对待长辈态度","对待挑衅自己的人的态度"])
# print(parser.get_format_instructions())
# The output should be formatted as a XML file.
# 1. Output should conform to the tags below.
# 2. If tags are not given, make them on your own.
# 3. Remember to always open and close all the tags.
#
# As an example, for the tags ["foo", "bar", "baz"]:
# 1. String "<foo>
#    <bar>
#       <baz></baz>
#    </bar>
# </foo>" is a well-formatted instance of the schema.
# 2. String "<foo>
#    <bar>
#    </foo>" is a badly-formatted instance.
# 3. String "<foo>
#    <tag>
#    </tag>
# </foo>" is a badly-formatted instance.
#
# Here are the output tags:
# 输出内容应该被格式化为一个 XML 文件。
t1 = ChatPromptTemplate.from_template("给我生成一个西格玛男人操作手册,{format_introduce}")
prompt = t1.partial(format_introduce = parser.get_format_instructions())#这里只要 xml解析器的格式介绍
print(prompt.format())

import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
# llm = ChatDeepSeek(
#     model=os.getenv("MODEL_NAME"),
#      temperature=0.8)
llm = ChatOpenAI(
    model=os.getenv("MODEL_NAME"), #注意,环境变量要有:HUNYUAN_SECRET_ID
     temperature=0.8)
chain = prompt | llm | StrOutputParser()
# chain = prompt | llm | parser #xml解析器会把返回结果变成字典
ai_msg = chain.invoke({})
print("ai_msg=",ai_msg)
print("type(ai_msg)=",type(ai_msg))
import json

# jsonStr = json.dumps(ai_msg, ensure_ascii=False, indent=2)
# print("jsonStr=",jsonStr)

