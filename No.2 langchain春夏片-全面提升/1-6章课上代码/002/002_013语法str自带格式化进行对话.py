# 三 个单引号 ''' 或者三个双引号 """
# 创建的字符串可以带换行
# str1:str = """
# 你好,我叫吉良吉影
# 你打扰我睡觉了
# """
# str1:str = '''
# 你好,我叫吉良吉影
# 你打扰我睡觉了
# '''
#
# print(str1)
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

#字符串里面用空的{}占位,后面用format可以格式化填充
# str2:str = """
# 你好,我叫{}
# 你打扰我{}了
# """
# print(str2)
# name = "吉良吉影"
# action = "睡觉"
# resultStr = str2.format(name,action)
# print(resultStr)

#空{}占位,后面用%和()填充,%d是int,%s是 字符串
str3:str = """
你好,我叫吉良吉影
你打扰我睡觉了
晚上11点开始熬夜,熬足个%d小时,早上%d点,我刚开始躺下%s,你就起床定了当啷懂了当啷开始刷牙洗脸敲洗脸盆
搞得人家没法睡觉了
""" % (9,8,"刷手机")
print(str3)
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(str3)
print(res.content)