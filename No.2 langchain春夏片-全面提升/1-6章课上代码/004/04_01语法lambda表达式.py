

fun1 = lambda a: a + 1 #冒号左边是 关键字和 传入参数,冒号右边是 要运行的表达式
result = fun1(1)
print(result)
#上面相当于下面的fun2
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
def fun2(a):
    return a+1
result = fun2(1)
print(result)

#可以多参数
fun2 = lambda a,b,c : a+b+c
result = fun2(1, 1, 1)
print(result)

# lambda (a,b) : a+b # lambda表达式的元组的参数不能再python3中使用
# (a,b) = 1,2
# print(a,b)
tuple1 = (1, 2, 3)#元组的下标操作,可以从[0]开始
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
fun3 = lambda x : x[0]+x[1] #不能把元组解包后当做参数,但是可以把一个元组作为参数,然后用下标访问
result = fun3((2,2) )
print(result)
