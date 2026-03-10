void fun(){

}
main(){

   Function fn = fun;
   print(fn);//通过打印可以看到 Function变量就是closure闭包

  //闭包捕获变量,在一个方法中,通过return 返回一个匿名方法,这个匿名方法会捕获他外层的变量,return 时被外面的Function类型的变量保存


  var fn1 = fun1();
   fn1();
   fn1();
   // print("fn2=======");
   // Function fn2 = fun1();
   // fn2();
   // fn2();
   // fn2();
  
  runFun1(fn1);
   runFun1(fn1);
   runFun1(fn1);
}
fun1(){
  int i = 0;
  return (){
     i++;
     print("i = $i");
  };
}
runFun1(Function fn){
  fn();
}