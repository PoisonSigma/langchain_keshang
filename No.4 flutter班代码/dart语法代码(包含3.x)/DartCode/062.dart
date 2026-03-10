import "dart:async";
import "dart:io";
import "dart:isolate";

main() {
  //assert断言，只要括号里面的表达式结果不是true，代码就不会继续执行，除非有try catch
  // assert(true);
  // assert(false);

  int a = 10;
  // assert(a > 100);
  //逻辑与 && ，左右表达式同时成立才返回true
  //逻辑或 || 左右表达式，有一个true就返回true，如果左边的表达式成立，右边的表达式就不用判断了，因为左边已经是true了
  // assert( a> 5 && a < 11 );
  // assert(a > 5 || a > 100 );
  // assert(a > 50 || a  <  11 );

  //用try catch捕获assert 失败的断言
  // try {
  //   assert(false);
  // } catch (e) {
  //   print("e=$e");
  // }
//throw（）括号里面放上异常，可以抛出异常
  try {
    // throw (FormatException("自定义的异常1"));
    // throw (IntegerDivisionByZeroException);//被0除的异常
    // throw(UnsupportedError);
    throw (IOException);
    // throw(IsolateSpawnException);
    // throw( TimeoutException);

    // throw new OutOfMemoryError();//new可以省略
    // throw  OutOfMemoryError();
    // int a = 11;
    // int b = 0;
    // // int b = 2;
    // // var result = a / b;
    // var result = a ~/ b; //除法取整数部分
    // print(result);
  }on UnsupportedError catch (e) {
  // on IntegerDivisionByZeroException catch(e){


    print("UnsupportedError e =$e");
  } on OutOfMemoryError catch (e) {
    print("OutOfMemoryError e =$e");
  } catch (e) {
    print("最后的cache e=$e");
  } finally {
    print("finally 最后执行到这里");
  }
  print("end");
}
