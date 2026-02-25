#def 定义 函数 不用加类型限定给参数，如果加，是用：冒号和类型，
# 不使用{}大括号当做函数体，而是使用缩进
def add(a:int, b:int)->int:
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b