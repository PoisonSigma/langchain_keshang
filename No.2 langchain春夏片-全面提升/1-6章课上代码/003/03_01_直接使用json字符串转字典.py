import json
json_str = '{"name": "张三", "age": 18,"money":9999}'#加入这个是llm传回的字符串,符合json格式
# name = json_str["name"]#字符串不能直接反问key
# print(name)
dic = json.loads(json_str)
print(dic)# 输出原始字典
print(dic['age'])
print(dic['name'])
print(dic['money'])


# JSON 字符串：
# python
# json_str = '{"name": "张三", "age": 18}'  # 双引号包裹的字符串
# JSON 对象（Python 中对应字典）：
# python
# json_obj = {"name": "张三", "age": 18}  # 字典类型
