main() {
  // 1.List.forEach()方法,是List里面封装的方法
  //forEach的参数要的是一个void Function(int) action  返回空,参数为一个参数的函数
  var l1 = [1, 2, 3, 4];
  //
  l1.forEach((element) {
    print(element);
  });
  //把方法名当做方法来调用,把函数名当做函数来调用
  l1.forEach(fn1); //给函数名,跟上面匿名函数一样,他会把每次遍历的值做为参数传给fn1
  /*
  相当于
  l1.forEach( fn1(v){
   print("fn1()调用v=$v");
    })

    */
    var l2 = ["abc","xxx"];
    l2.forEach(fn2);  //这里要的类型是 void Function(String) action ,根据l2的泛型 <String>自动要一个参数,类型是String的 函数


  //Map的forEach要的参数是void Function(类型, 类型)    ,例如下面要的是参数是(String,Object)的函数
  var m1 = {"name": "张三", "age": 18};
  m1.forEach((key, value) {
    print("key=$key value=$value");
  });
  m1.forEach(fn3);
}

//void 参数列表为1个参数
fn1(int v) {
  print("fn1()调用v=$v");
}
fn2(String str){
  print("fn2()调用str=$str");
}
fn3(String k,Object v){
  print("k = $k v = $v");
}