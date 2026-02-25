from datetime import datetime
import os

from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_deepseek import ChatDeepSeek
#partial 部分的, 把已经存在的模板,填充一部分,返回新的模板
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"))
# t1 = ChatPromptTemplate.from_template("告诉我城市{city}的天气预报",partial_variables = {"time":"3月21日"})
t1 = ChatPromptTemplate.from_template("告诉我城市{city}{road}路的天气预报,时间是{time}")
# t1 = PromptTemplate.from_template("告诉我城市{city}{road}路的天气预报,时间是{time}")
# partial ,返回一个新的模板
# template.partial(user="Lucy", name="R2D2")
print(t1)
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))#需要包含from datetime import datetime
t2 = t1.partial(time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")) #此时时间已经被填充,用户只需要填写一部分城市
print(t2)
t3 = t2.partial(road="大呲花")
print(t3)
t4 = t3.partial(city = "哈尔滨")
print(t4)
msg = t4.format()
print(msg)#ChatPromptTemplate 默认会添加Human
