#安装包:langchain-tavily
import warnings
# 过滤Tavily的属性覆盖警告TavilyResearch 类（TavilySearch 的底层实现类）中的 output_schema 和 stream 字段名称，与父类 BaseTool 的同名属性重复；
warnings.filterwarnings("ignore", message="Field name .* shadows an attribute in parent")

from langchain_tavily import TavilySearch
from dotenv import load_dotenv
load_dotenv("openai.env")
tool = TavilySearch(max_results = 2)


result = tool.invoke("今天几号?")
print(result)

