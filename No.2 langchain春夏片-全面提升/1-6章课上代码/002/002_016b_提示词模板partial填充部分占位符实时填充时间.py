from datetime import datetime #时间用
#partial 部分的, 把已经存在的模板,填充一部分,返回新的模板
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
# t1 = PromptTemplate.from_template("告诉我城市{city}{road}路时间是{time},的天气预报") #默认生成带Human:的字符串
t1 = ChatPromptTemplate.from_template("告诉我城市{city}{road}路时间是{time},的天气预报") #默认生成带Human:的字符串
print(t1)
t2 = t1.partial(road = "大呲花")
print(t2)
# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
t3 = t2.partial(time = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(t3)
msg = t3.format(city="哈尔滨")
print(msg)
# msg = t2.format(city = "哈尔滨" ,time = "1月1日")
# print(msg)
# t2.partial()

