import threading

def fun1(num):
    print("线程开始:",num,end="结束了\n")
    for i in range(100):
        print(num,":",i,end="结束了\n")

# 直接调用了函数 fun1，而非将函数作为参数传递给线程。这会导致：
# 函数在主线程中立即执行，而非在线程中执行。
# 线程的 target 参数被错误设置为函数的返回值（None），导致线程实际未执行任何操作。
# thread1  = threading.Thread(fun1(1))#错误,没有加入线程
# thread2  = threading.Thread(fun1(2))#错误,没有加入线程

thread1  = threading.Thread(target=fun1,args=(1,))
# 错误 :参数不能是1而是1,: thread1  = threading.Thread(target=fun1,args=(1))#错误,1是int, 1,是元组
thread1.start()
a = 2, #这个类型是元组
thread2  = threading.Thread(target=fun1,args=(a))
thread2.start()

thread1.join()#等待线程执行完才向下执行
thread2.join()
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
