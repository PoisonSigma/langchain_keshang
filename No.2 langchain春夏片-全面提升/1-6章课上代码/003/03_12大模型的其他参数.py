#deepseek不限速:
# https://api-docs.deepseek.com/zh-cn/quick_start/rate_limit
import os

from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
limiter = InMemoryRateLimiter(  # 注意deepseek官网显示,不限制调用时间间隔,这里无效
    requests_per_second=2,  # 每1秒请求一次
    check_every_n_seconds=0.1,  # 每100毫秒检查一次
    max_bucket_size=2,  # 控制最大突发大
)
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"),
                   timeout=30,  # 意味着在向 DeepSeek 模型发送请求之后，如果在 30 秒内没有收到响应，就会触发超时异常
                   max_tokens=200,  # 最大token数字
                   stop="好",  # 停止的字符,这样返回的就只有4个,就问你扣不抠门
                   max_retries=2,
                   # 最大重试次数,在与大语言模型进行交互时，因为网络问题、服务器过载或者其他不可控的因素，请求有可能会失败。max_retries 能够让程序在请求失败时尝试重新发送请求，直至达到最大重试次数。
                   rate_limiter=limiter

                   )
res = llm.invoke("你好")
print(res)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print(res.content)