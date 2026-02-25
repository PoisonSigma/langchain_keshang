#元组解包（Tuple Unpacking），也叫元组解构，
# 是 Python 中一种方便的语法特性，
# 它允许将一个元组中的元素一次性赋值给多个变量。
from keyword import kwlist
#
# item1 = (1,2,"abc")
# (a,b,c) = item1
# print(a)
# print(b)
# print(c)
def add(**kwargs):
    # for item in kwargs.items():
    #     print(item)
        # (a1,a2) = item
        # print(a1)
        # print(a2)
    for v in kwargs.values():
        print(v)
add(s1=123,s2=456,s3=789)