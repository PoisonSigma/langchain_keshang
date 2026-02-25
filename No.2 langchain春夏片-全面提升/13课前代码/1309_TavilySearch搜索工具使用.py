from langchain_tavily import TavilySearch
#TavilySearch 费用每月1000次免费,超出部分30美元4000次,30*7.18 / 4000= 0.05385
#或者 $0.008 每次 0.008*7.18= 0.05744人民币每次
#langserch费用 超出免费部分 0.036 元 / 次
from dotenv import load_dotenv
load_dotenv("openai.env")
#要在环境变量里面设置:TAVILY_API_KEY
tool = TavilySearch(max_results=1)
tools = [tool]
result = tool.invoke("今天几号?")
print(result)

