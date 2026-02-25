from typing import Iterator
# 迭代器是一种对象，它允许你逐个访问集合（如列表、元组、字典等）中的元素，而不需要提前将整个集合加载到内存中。迭代器提供了一种统一的方式来遍历不同类型的集合，使得代码更加通用和灵活。
# 迭代器协议
# 在 Python 中，一个对象要成为迭代器，必须实现两个特殊方法，这两个方法构成了迭代器协议：
# __iter__() 方法：该方法返回迭代器对象本身。当你使用 for 循环或其他迭代操作时，首先会调用这个方法来获取迭代器。
# __next__() 方法：该方法返回迭代器的下一个元素。如果没有更多元素可供迭代，它会抛出 StopIteration 异常，表示迭代结束。

# r = range(1,10)
# print(r)
# l1 = list(r)
# print(l1)
print(list(range(10)))
# l1 = [1, 2, 3]
# it1:Iterator[int] = iter(l1)
# print(it1)
# res = it1.__next__()
# print(res)
# res = it1.__next__()
# print(res)
# res = it1.__next__()
# print(res)
# #next走到最后的时候,报错:StopIteration
# res = it1.__next__()
# print(res)
#
# l2 = ["a", "b", "c","d"]
# l2.append("e")
# # it2:Iterator[str] = iter(l2)
# it2 = iter(l2)
# # print(next(it2))
# # print(next(it2))
# # print(next(it2))
# # print(next(it2))
# # print(next(it2))
# for item in it2:
#     print(item)
# print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
#
# for item in it2:
#     print(item)
# # next(it2)#for in遍历结束,再next往后走会报错
# # 在 Python 里，以双下划线开头和结尾的方法被称为特殊方法或者魔法方法（Magic Methods）。__next__ 方法就属于这类特殊方法，它是迭代器协议的关键组成部分。当一个对象实现了 __next__ 方法，就意味着这个对象遵循了迭代器协议，可作为迭代器使用。
#
# # for item in it1:
# #     print(item)
# # print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
# # for item in it1:
# #     print(item)
# # print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
#
# # for item in l1:
# #     print(item)
# # print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
# # for item in l1:
# #     print(item)