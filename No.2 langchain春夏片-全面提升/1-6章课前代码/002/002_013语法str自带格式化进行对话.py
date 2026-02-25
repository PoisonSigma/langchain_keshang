
import os
from typing import Any

from dotenv import load_dotenv
from langchain_core.prompts import StringPromptTemplate
from langchain_core.prompts.base import FormatOutputType
from langchain_openai import ChatOpenAI

# 三 个单引号 ''' 或者三个双引号 """
# 创建的字符串可以带换行

#
# name = """吉良吉影"""
# #字符串中使用%s作为占位,后面传入字符串,进行格式化
# time = 7
# str1 = """
# 你好,我是%s
# 你打扰我睡觉了
# 早上%d点,我刚躺下,你就起床叮了当了咚了当啷的做饭,是不是有点扰民了呀?
# """ %(name, time)
# print(str1)
# str2 = """
# 你好,我是%s
# 你打扰我睡觉了
# 早上%d点,我刚躺下,你就起床叮了当了咚了当啷的做饭,是不是有点扰民了呀?
# """ %("吉良吉影", 8)
# print(str2)
# #字符串可以使用空的{}占位,后面接上.format传入的值进行格式化
str3 = """
你好,我是{}
你打扰我睡觉了
早上{}点,我刚躺下,你就起床叮了当了咚了当啷的做饭,是不是有点扰民了呀?
"""
resultStr = str3.format("吉良吉影",8)
print("戟把离手越进义父离你越远>---红字增幅+25----------)三(--> ")
print(resultStr)
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(resultStr)
print(res.content)


