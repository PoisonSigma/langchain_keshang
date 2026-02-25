#下面是json解构的字典,不是json解构的字符串
#注意,下面的字典,在python中正确,但是要是在网上的json格式化网页,
# 需要把每个元素多余逗号去掉
import json

from langchain_core.prompts import ChatPromptTemplate

json_schema_dic = {
"title": "ZhouZhou",
    "description": "保存JoJo的奇妙冒险中人物姓名和年龄",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "保存JoJo的奇妙冒险中人物姓名"
        },
        "age": {
            "type": "integer",
            "description": "年龄"
        }
    },
    "required": ["name", "age"]
}
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    stop = "好",
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)

stru_llm = llm.with_structured_output(json_schema_dic)#给结构化输出传入json字典
prompt = ChatPromptTemplate.from_template("告诉我{count}个名字")
chain = prompt | stru_llm
ai_msg = chain.invoke({"count":2})
print("ai_msg=",ai_msg)
jsonStr = json.dumps(ai_msg, ensure_ascii=False, indent=2)
print("jsonStr=",jsonStr)
print("type(ai_msg)=",type(ai_msg))

