import 'dart:async';
import 'dart:io';
import 'dart:isolate';

main() {
//assert断言，只要括号里面的表达式结果不是true，代码就不会继续执行，除非有try catch
  int a = 10;

  // assert(false);//抛出异常，因为结果是false
  // assert(a> 11);//抛出异常
//逻辑与 && ，左右表达式同时成立才返回true

// assert( a > 5 && a < 11);
//逻辑或 || 左右表达式，有一个true就返回true，如果左边的表达式成立，右边的表达式就不用判断了，因为左边已经是true了
  assert(a > 5 || a > 100); //左边表达式true，所以不判断右边的a > 100 了

  //用try catch捕获assert 失败的断言
  try {
    // assert(false);
  } catch (e) {
    print("e=$e");
  }

  //throw（）括号里面放上异常，可以抛出异常
  // throw (FormatException("自定义的错误"));//抛出自定义的异常
  // try {
  //   throw (FormatException("自定义的错误")); //允许传入一个 message字符串
  // } catch (e) {
  //   print("e=$e");
  // }

  //try on catch，on可以把异常分成不同类型去捕获
  try {
    // throw (IntegerDivisionByZeroException);
    // throw(IOException);
    // throw(IsolateSpawnException);
    throw(TimeoutException);
    throw (FormatException("自定义的错误2"));


    throw new OutOfMemoryError();//new可以省略
    // throw  OutOfMemoryError();
    int a = 100;

    // int b = 2;
    // int b = 0;//用来测试除数为0的异常
    // var result = a~/b;// ~/除法取整，只保留整数部分，用取整除或抛出异常
    // // var result = a/b;//用/除法不会抛出异常，会得到结果无限大
    // print("result = $result");


  } on FormatException catch (e) {
    print("on FormatException e=$e"); //第一个on 接收到了，那么下面的on就不再捕获了
  } on IntegerDivisionByZeroException catch (e) {
    // IntegerDivisionByZeroException已经废弃，用UnsupportedError代替
    print("IntegerDivisionByZeroException e=$e");
  } on UnsupportedError catch (e) {
    print("UnsupportedError e=$e");
  }
  on Exception catch (e) {
    print("on Exception e=$e");
  }
  // on OutOfMemoryError catch(e){
  //   print("on OutOfM
  //   emoryError e=$e");
  // }
  catch (e) {
    //捕获全部的
    print(" catch e=$e");

  }finally{
    //执行完catch 以后执行finally
    print("finally执行");
  }

  print("end");
}