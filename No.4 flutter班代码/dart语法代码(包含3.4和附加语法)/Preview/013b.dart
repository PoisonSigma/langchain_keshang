int add(int a ,int b){
  print("add执行 ${a+b}");
  return a+b;
}
run(Function fn){  //这个函数可以作为参数,这种方法没有指定传入的函数 参数类型和返回值类型
  fn(1,3);//调用函数指针里面保存的函数//直接给参数写Function 这种用法无法确定传入的函数是哪种类型
  // fn(1,2,3);//编译不报错,运行保存,因为传入的是 2个参数的类型,3个参数的类型没有传入.
}
//下面是明确给函数指定了函数的返回类型和参数类型,这种情况可以让编译器在编译阶段就发现传入的参数类型不对,不能随便传
run2(int Function(int a,int b) fn ){
 // fn(1,2,3);//错误,明确指出,函数的返回值和参数类型,不是3个参数
   var result = fn(1,2);
   print("run2 result= $result");
}


//使用typedef 定义一个函数类型,c++的函数签名
typedef Add = int Function (int,int);
run3(Add fn){
   var result = fn(1,2);
   print("run3 result= $result");
}
//匿名函数作为返回值

Add run4(){

  return (a,b){
    return a+b;
  };
}

main(){
  //Function函数指针,保存函数的地址,调用函数的方法是()小括号
    Function fn = add;//把函数名赋值给Function
   int result =  fn(1,3);//调用函数
    // fn(1,2,3);//编译通过,但是调用的时候,报错,参数类型不对
    print(result);
    var fn2 = add;//自动推断出fn2的类型是 int Function(int, int) ,这个推断出来的类型刚好是他的函数签名,函数签名就是c++里面去掉参数名的函数类型

      run(fn); // 调用

    // run2(1);//run2明确参数类型,不能乱传
  run2((a, b){
    print("匿名函数2执行 a+b = ${a+b}");
    return a+b;
  });

  run3((p0, p1) => p0+p1);
  var  result4 = run4()(1,2);//调用返回的函数
  print("result4 = $result4");
}