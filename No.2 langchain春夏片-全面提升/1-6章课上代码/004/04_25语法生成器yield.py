#generator生成器
# yield 生成
#yield 可以单独返回一个内容, 保存在generator生成器里面,每次next(generator),都会返回下一个yield 返回的内容
#yield必须放在方法里面,返回generator,是给方法用的,跟__next__和__iter__区别是,__next__和__iter__是给class用的

def fun1():
    yield "你"
    yield "好"  #返回类型是 generator
    yield "啊"
    yield "我叫赛利亚"
    yield "今晚"
    yield "上"
    yield "泡面的"
    yield "钱"
    yield "我来出"
    yield "把你的手机给我,这是你的备用金"
    # while True:
    #     yield 1
g1 = fun1()
print(g1)
print(type(g1)) #类型是generator
# g2 = yield "好"  #错误不能在函数外用
# result = next(g1)
# print(result)
# result = next(g1)
# print(result)
# result = next(g1) #报错,生成器已经耗尽,没有更多的yield生成值了
# print(result)
for item in g1:
    print(item)

print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

str1 = "你好啊,我叫赛利亚" #str字符串也可以迭代,每个字符都是可以迭代
for item in str1:
    print(item)
it2 =iter(str1) #字符串转迭代器,以后可以调用next,跟range转迭代器一样
result = next(it2)#转为迭代器就能next
print(result)

