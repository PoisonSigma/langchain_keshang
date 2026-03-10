main(){
  //Future的类型限定,泛型
    var f1 = Future<String>.value("abc");
    // var f2= Future<String>.value(123);//报错,类型不匹配
  var f3 = fun1();
  f3.then((value) => print(value));
}


//Future作为返回类型
 Future fun1(){
  return Future<String>.value("abc");
}