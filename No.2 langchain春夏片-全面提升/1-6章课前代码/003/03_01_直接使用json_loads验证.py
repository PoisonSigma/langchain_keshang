# 直接使用 json.loads
# python
import json

json_str = '{"name": "张三", "age": 18,"money":9999}'#加入这个是llm传回的字符串,符合json格式
data_dict = json.loads(json_str)
print(data_dict)  # 输出原始字典