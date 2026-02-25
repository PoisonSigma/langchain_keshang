import asyncio
import os
import time
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv


async def fun1():
    print("===开始===")
    start_time = time.time()
    l1 = await llm.ainvoke("你好")
    end_time = time.time()
    print("==结束===")
    print(f"本次请求耗时: {end_time - start_time} 秒")
    print(l1.content)


load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    timeout=30,
    max_tokens=200,
    stop="好",
    max_retries=2,
    rate_limiter=InMemoryRateLimiter(
        requests_per_second=2,
        check_every_n_seconds=0.1,
        max_bucket_size=2,
    )
)


async def main():
    for i in range(1, 10):
        print(f"i= {i}")
    tasks = [fun1() for _ in range(5)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
