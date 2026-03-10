void fun(){
}
main() {
/*
  Function  fn = fun;
  print(fn);//通过打印可以看到 Function变量就是closure闭包

  //闭包捕获变量,在一个方法中,通过return 返回一个匿名方法,这个匿名方法会捕获他外层的变量,return 时被外面的Function类型的变量保存

  fun1(); //直接调用fun1()并没有执行里面的闭包,因为闭包是return回来的
  fun1();
  fun1();
  var fn1 = fun1();//把闭包赋值给一个变量
  // fn1();//这里相当于执行了 里面return回来的匿名函数
  // fn1();
  // fn1();

  // fun2();//里面的匿名方法执行了,但是i没有被保存,需要外面有一个Function变量保存闭包
  // fun2();
  // fun2();

  var fn2 = fun2();
  fn2();
  fn2();
  //被捕获的变量并不是全局变量,只是通过外面接受的Function变量保存下来

  print("fn2b=======");
  var fn2b = fun2();
  fn2b();
  fn2b();

  runFun2(fn2);
}
fun1(){
  int i = 0;
  return (){
    i++;
    print("i=$i");
  };
}
fun2(){
  int i = 0;
  return (){
    i++;
    print("i=$i");
  };
}
runFun2(Function fn){

  print("runFun2()执行");
  //传入进来的fn2,依然保存着
  fn();
  fn();
  var fn3 = fun2();//这里重新申请的fn3里的i就是从0开始
  fn3();
  fn3();

 */


  // 创建一个将 2 添加的函数。
  var add2 = makeAdder(2);

  // 创建一个将 4 添加的函数。
  var add4 = makeAdder(4);

  print(add2(3) == 5);
  print(add4(3) == 7);
}



/// 返回一个将 [addBy] 添加到函数参数的函数。
Function makeAdder(int addBy) {
  return (int i) => addBy + i;
}
