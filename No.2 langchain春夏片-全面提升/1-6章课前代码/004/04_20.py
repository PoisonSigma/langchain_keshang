from typing import Iterator

from langchain_core.runnables import RunnableGenerator

list1 = range(1,3)
# for item in list1:
#     print(item)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

it1 = iter(list1)#把range转为迭代器
i1 = next(it1)
print(i1)
i1 = next(it1)
print(i1)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

for item in it1:#for...in 能遍历迭代器
    print(item)

#下面是自己做一个可迭代的对象
class PsRange:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.current = start
    def __iter__(self):
        return self #让自己可以迭代
    def __next__(self):#让外面可以调用next(ps1)
        if self.current < self.end:
            value = self.current #先保存+1之前的值,为了返回
            self.current += 1
            return value
        else:
            raise StopIteration #抛出异常,代表迭代停止了,到最后了
ps1 = PsRange(1,3)
result1 = next(ps1)
print(result1)
result1 = next(ps1)
print(result1)
# result1 = next(ps1)
# print(result1)

def psStream():
        yield "你" #使用yield关键字会返回 generator 生成器, 也是一种迭代器,每次调用next会返回单个结果
        yield "好"
        yield "啊"
        yield "今晚"
        yield "上"
        yield "泡面的"
        yield "钱"
        yield "省下"
        yield "了"

iterator1 = psStream()
r1 = next(iterator1)
print(r1)
r1 = next(iterator1)
print(r1)
r1 = next(iterator1)
print(r1)
for item in iterator1:
    print(item)
# r1 = next(iterator1) #for in 报错 遍历完迭代器,再往后迭代,会报错
# print(r1)



