import json
json_schema_dic = {
    "name":"王二狗",
    "age":18
}
json_schema_dic = { #json解构的字典
    'name':'王二狗',
    'age':18
}

jsonStr = json.dumps(json_schema_dic, ensure_ascii=False, indent=2)
print("jsonStr",jsonStr)
jsonStr2 = """{
  "name": "王二狗",
  "age": 18
}""" #json解构的字符串

print("jsonStr2",jsonStr2)