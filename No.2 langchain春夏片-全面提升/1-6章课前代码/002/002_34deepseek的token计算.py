#解释器安装包:langchain_deepseek
import os

from dotenv import load_dotenv
from langchain_deepseek import  ChatDeepSeek
import  os
#注意deepseek,如果使用默认的api base 那么DEEPSEEK_API_KEY要被设置
# If using default api base, DEEPSEEK_API_KEY must be set
load_dotenv(dotenv_path="../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
res = llm.invoke("你好")
print(res.content)
print("response_metadata = ",res.response_metadata)
print("response_metadata = ",res.response_metadata)
print("输入含命中和未命中缓存",res.response_metadata["token_usage"]["prompt_tokens"])
print("返回,输出",res.response_metadata["token_usage"]["completion_tokens"])
print("总共",res.response_metadata["token_usage"]["total_tokens"])



#response_metadata 是BaseModel里面的成员
#completion_tokens:回答文本同样会被拆分成 Token，这些 Token 的数量就是 completion_tokens
#prompt_tokens提示词,相当于输入的tokens数字
#total_tokens:总共的tokens数字

