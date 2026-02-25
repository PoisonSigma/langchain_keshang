from langchain_core.prompts import ChatPromptTemplate
import json
json_schema_dic = {
"title": "ZhouZhou", #理解为类名
    "description": "保存JoJo的奇妙冒险中人物姓名和年龄", # 理解为描述信息,就是doc string
    "type": "object", #类型对象
    "properties": {
        "name": {#key的名字
            "type": "string",#类型字符串
            "description": "保存JoJo的奇妙冒险中人物姓名"#描述信息
        },
        "age": {#key的名字
            "type": "integer",
            "description": "年龄"
        }
    },
    "required": ["name", "age"]#必填字段
}
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    stop = "好",
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
stru_llm = llm.with_structured_output(json_schema_dic)
prompt = ChatPromptTemplate.from_template("给我{count}个名字")
chain = prompt | stru_llm
ai_msg = chain.invoke({"count":2})
print("ai_msg=",ai_msg)
print("type(ai_msg)=",type(ai_msg))

#字典转json字符串

jsonStr = json.dumps(ai_msg, ensure_ascii=True, indent=2)
print("jsonStr=",jsonStr)
