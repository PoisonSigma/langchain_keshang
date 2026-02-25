import asyncio
import threading

# 准备把下面函数加入线程
def fun1(num):
    for i in range(10):
        #想在这里睡眠1秒
        print(num,":",i)




# 直接调用了函数 invoke1 和 invoke2，而非将函数作为参数传递给线程。这会导致：
# 函数在主线程中立即执行，而非在线程中执行。
# 线程的 target 参数被错误设置为函数的返回值（None），导致线程实际未执行任何操作。
#thread1 = threading.Thread(fun1(1))#错误,这种方法,会把整个函数放在主线程里运行,没有
# thread1 = threading.Thread(target = fun1 ,args =(1))#错误,参数不是元组,改为(1,)
thread1 = threading.Thread(target = fun1 ,args =(1,))#错误,参数不是元组,改为(1,)
thread1.start()
thread2 =threading.Thread(target = fun1 ,args =(2,))
thread2.start()
# 等待所有线程完成
thread1.join()#等待线程执行完才向下执行
thread2.join()
print("All threads have finished.")