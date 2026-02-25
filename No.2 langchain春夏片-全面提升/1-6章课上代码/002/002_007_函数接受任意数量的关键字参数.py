# **kwargs: Any 是类型注解，用于提示 **kwargs 可以接受任意类型的值。类型注解本身不会影响代码的运行，只是提供给开发者和静态类型检查工具（如 mypy）的提示信息。
from typing import Any


def fun1(a: int, **kwargs: Any):
    # print(kwargs)
    # print(kwargs["b"])
    # print(kwargs["c"])
    # print(kwargs["additional_kwargs"])
    for k, v in kwargs.items():
        # print(f"{k} = {v}")
        print(k)
        print(v)


fun1(a=100, b=200, c=300, additional_kwargs={"你的名字是": "吉恶吉懂事"})
