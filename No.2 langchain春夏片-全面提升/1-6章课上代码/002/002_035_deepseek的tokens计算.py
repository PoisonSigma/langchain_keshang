#解释器安装包:langchain-deepseek
#注意安装包中间是-,不是下划线
import os

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
load_dotenv("../assets/openai.env")
# print(os.getenv("MODEL_NAME"))
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"))
res = llm.invoke("wu wa e wa mou xin dei yi lv")
print("res.content=",res.content)
print(res.response_metadata)
#response_metadata 是BaseModel里面的成员

#completion_tokens:回答文本同样会被拆分成 Token，这些 Token 的数量就是 completion_tokens
#prompt_tokens提示词,相当于输入的tokens数字
#total_tokens:总共的tokens数字



