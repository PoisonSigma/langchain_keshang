import os
from pprint import pprint

path = os.getenv("PATH")
# print(path)
#os.pathsep 是 Python os 模块提供的跨平台 PATH 分隔符常量—— 它本质是一个字符串，值会根据你的操作系统自动适配，专门用来分割系统 PATH 环境变量里的多个路径。
# print(f"os.pathsep=${o用s.pathsep}")
# # str1 = "123,456"
# #
# # list1 = str1.split(",")#逗号分隔字符串变成list

# for item in list1:
#     print(item)

list2 = path.split(os.pathsep)
for item in  list2:
    print(item)