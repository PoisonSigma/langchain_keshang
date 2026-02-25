# 自己模拟一个流失输出的原理 使用 RunnableLamada和  yield 生成 generator
#yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
#执行yield返回 generator生成器,生成器可以被迭代,每次 next获取下一次yield返回的值
import time

from langchain_core.runnables import RunnableLambda


def fun1(str1: str):
    print("fun1执行")
    if (str1.find("金卡") == -1) and (str1.find("饭") == -1):
        # python里面逻辑与不是&& 而是and ,逻辑或不是|| 而是 or
        yield "心中无女人,拔刀自然神"
        yield "第一套西格玛儿童广播体操"
        yield "现在开始做"
        yield "1234"
        yield "2234"
        yield "3234"
        yield "4234"
    else:
        print("else执行")
        raise ValueError("找到金卡或者饭")
g1 = fun1("阿斯顿发山东第三方")
print(g1)
print(type(g1))
# result = next(g1)
# print(result)
# result = next(g1)
# print(result)
# result = next(g1)
# print(result)
# for chunk in g1:
#     print(chunk)
# stream("我给你我的金卡,然后还去你家做饭")
def error_fun1(str1: str):
    # print("error_fun2执行")
    # print("你在教我做事啊,在我面前不许说我兄弟坏话")
    yield "你在教我做事啊"
    yield "在我面前不许说我兄弟坏话"
    # raise ValueError #这里模拟stream不能处理的东西,就是强行抛出一个异常
runable1 = RunnableLambda(fun1)
runable2 = RunnableLambda(error_fun1)
chain = runable1.with_fallbacks([runable2])
# result = chain.invoke("asdsadfdsf")
# print(result)
# print(type(result))
# for character in result: #invoke返回最终组合的字符串结果,str类型也能被for in 遍历
#     print(character)

result = chain.stream("我给你我的附属金卡")
# result = chain.stream("你好")
# print(result)
# print(type(result))
# print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
#
# str1 =  next(result)
# print(str1)
# str1 =  next(result)
# print(str1)
for chunk in result:
    time.sleep(1)
    print(chunk,end="")
