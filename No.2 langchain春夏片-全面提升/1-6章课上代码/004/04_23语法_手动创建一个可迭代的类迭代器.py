# for i in range(9):
#     print(i)
result = range(9)
result = range(2, 5)
# print(result)
# print(type(result))
# for chunk in result:
#     print(chunk)
# next(result). #有这个方法才能next __iter__ __next__ 重写这2个方法才能在外面next调用
it1 = iter(result)
# print(it1)
# print(type(it1))
# 迭代器刚开始指向开头,每次next,会返回当前指向的位置,然后往后移动一下,
# 直到遇到 手动抛出异常 raiseStopIteration
# 或者,真的到最后了,后面没有可以迭代的了,会自动 raiseStopIteration
result = next(it1)
# print(result)
# print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
# for chunk in it1:
#     print(chunk)
# result = next(it1) #for in 会自动跌倒到最后,再执行next就会报错

# print(type(result))
# result = next(it1)
# print(result)
# result = next(it1)
# print(result)


# result = next(it1)#报错,停止迭代StopIteration,到最后了
# print(result)
class MaZhi:   #(你叫润之,我叫 麻之)
    def __init__(self,start:int,end:int): #(MaZhi(2,5)
        self.start = start#开始位置
        self.end = end#结束位置
        self.current = start#当前位置
    def __iter__(self):
        return self #返回自己
    def __next__(self):
        print("调用next()方法")
        if self.current < self.end:#判断是否到结尾了
            value = self.current #先保存当前的值,后面要返回
            self.current += 1
            return value
        else:
            raise StopIteration #超出范围就手动抛出异常StopIteration
mazhi1 = MaZhi(2,5)
print(mazhi1)
# for chunk in mazhi1:
#     print(chunk)
result = next(mazhi1)
print(result)
result = next(mazhi1)
print(result)
result = next(mazhi1)
print(result)
# result = next(mazhi1)
# print(result)