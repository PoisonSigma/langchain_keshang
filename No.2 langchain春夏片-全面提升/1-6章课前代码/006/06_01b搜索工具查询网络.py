import os

import requests
import json
#区别在于url不同,一个是rerank,翻译过来叫重新排序,一个叫web-search,是网络搜索
url = "https://api.langsearch.com/v1/web-search"
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
payload = json.dumps({
  "query": "告诉我哈尔滨市2025年5月14日天气预报",#查询问题
  "freshness": "noLimit",
  "summary": True,
  "count": 1 #这个结果不要太多:
})
headers = {
  'Authorization':  os.getenv("LangSearchAPI"),
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
# 解析JSON响应
data = response.json()

# 提取结果列表（注意观察响应结构）
try:
  # 根据API返回的实际数据结构访问
  web_pages = data['data']['webPages']
  list1 = web_pages['value']

  print(f"找到 {len(list1)} 条结果：")
  for item in list1:
    print("\n标题:", item.get('name'))
    print("链接:", item.get('url'))
    print("摘要:", item.get('summary'))
    print("发布时间:", item.get('datePublished'))
except KeyError as e:
  print("响应数据结构异常，缺少关键字段:", e)
  print("完整响应内容：")
  print(json.dumps(data, indent=2, ensure_ascii=False))

