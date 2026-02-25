#元组解包（Tuple Unpacking），也叫元组解构，是 Python 中一种方便的语法特性，它允许将一个元组中的元素一次性赋值给多个变量。
#
# item1 = (1,3)
# item2:tuple[int,int] = (1,3) #定义一个元组
# (a,b) = item2 #元组解包
# print(a,b)
# print(item1)

def add( **kwargs):
    for item in kwargs.items():#items()是遍历的元组
        print(item)
        (k,v) = item #解构
        print(k,v)
        print("戟把离手越进义父离你越远>---红字增幅+25----------)三(--> ")

    for v in kwargs.values():#values遍历的是每次只有值
        print(v)

add(a=1,b=2,c=3)