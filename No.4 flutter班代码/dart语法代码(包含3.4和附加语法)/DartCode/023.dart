main(){
  // 1.List.forEach()方法,是List里面封装的方法
  //forEach的参数要的是一个void Function(int) action  返回空,参数为一个参数的函数
  //1.List.forEach
  /*
  var l1 = [1,2,3,4,5];
  for(var item in l1){
       print(item);
  }
  */
  //void Function(int) action
  var l1 = [1,2,3,4,5,"str"];
  // var l1 = ["str","abc"];
  l1.forEach((element) {
    // print("e= $element");
  });
  // l1.forEach(fn1);
  // l1.forEach(fn2);

  //Map的forEach要的参数是void Function(类型, 类型)    ,例如下面要的是参数是(String,Object)的函数
  var m1 = {
    "name":"张三",
    "age":18
  };
  m1.forEach((key, value) {
    // print("key = $key value = $value");
  });
  // m1.forEach(fn3);
  m1.forEach((String k, Object v){
    print("匿名函数代替fn3执行了 k = $k v = $v");
  });
}
fn1(Object v){
  print("fn1执行了 v = $v");
}
fn2(String str){
  print("fn2执行了 str = $str");
}
// fn3(String k, Object v){
//   print("fn3执行了 k = $k v = $v");
// }