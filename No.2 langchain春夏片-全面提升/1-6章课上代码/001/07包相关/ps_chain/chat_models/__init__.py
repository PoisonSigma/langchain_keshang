# __all__ 列表中的元素必须是字符串，且是模块中存在的对象名。
__all__ = [
    "name1", "add"
]
name1 = "zhang3"  # 定义一个字符串


def add(a, b):
    return a + b


def sub(a: int, b: int) -> int:
    return a - b
# result = add(1, 2);
# print(result)
# result = sub(10, 5);
# print(result)
