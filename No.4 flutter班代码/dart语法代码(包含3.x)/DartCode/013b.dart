

run(Function fn){
    fn();
}
run2(Add fn){
   var result =  fn(1,2);
   print("run2执行  result = $result");
}
int add (int a,int b){
  print("add()执行 a+b= ${a+b}");
  return a+b;
}
typedef Add = int Function  (int,int);

//把匿名函数当做返回值来使用
 Add run3(){
  //    Add fn = (a,b){
  //   return a+b;
  // };
  //    return fn;
   return (a,b){
     print("run3执行");
     return a+b;
   };
}

main(){
  //1.匿名函数定义完不会直接执行
  //2.把匿名函数结尾加()小括号,是直接执行匿名函数
  // (){
  //     print("匿名函数执行");
  //   }();
  //3.给普通的函数结尾直接加小括号,不可以被直接执行,如下:
    show(){
    print("show执行");
  };
  // var fn2 = show;
  // fn2();

  // 匿名函数当做参数

  //
  // run(  (){
  //   print("匿名函数执行了abc");
  // });
  // run(show);

  // run(add);//报错,调用的时候类型不匹配
  // run2((a,b) => a+b);
  run2((a,b){
    return a+b;
  });

    // run2(add);
    var result3 = run3()(1,2);
    print("result3 = $result3");
}