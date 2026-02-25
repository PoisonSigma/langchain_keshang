import os

path_original = os.getenv("PATH")
# print(path_original)
# print(f"{os.pathsep}")#当前平台路径分隔符是

list1 = path_original.split(os.pathsep)
for item in list1:
    print( item)