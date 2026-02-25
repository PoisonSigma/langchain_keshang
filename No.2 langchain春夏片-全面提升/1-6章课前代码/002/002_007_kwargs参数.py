from typing import  Any




# **kwargs: Any 是类型注解，用于提示 **kwargs 可以接受任意类型的值。类型注解本身不会影响代码的运行，只是提供给开发者和静态类型检查工具（如 mypy）的提示信息。
def fun1(**kwargs: Any):
    for k,v in kwargs.items():
        print(k)
        print(v)

fun1(a="abc",b=123,c=456)
