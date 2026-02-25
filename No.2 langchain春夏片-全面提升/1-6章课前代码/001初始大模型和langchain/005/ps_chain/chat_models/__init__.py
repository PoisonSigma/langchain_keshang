# __all__ 列表中的元素必须是字符串，且是模块中存在的对象名。
__all__ = [
    "add2",
    "ChatOpenAI2"
]
def add2(a,b):
    return a + b;
def ChatOpenAI2(model,temperature):
    print(model, temperature)