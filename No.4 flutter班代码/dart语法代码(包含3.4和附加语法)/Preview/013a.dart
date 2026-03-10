main() {



  //1.匿名函数定义完不会直接执行
  () {
    print("这是一个匿名函数,但是不会被执行");
  };

  //2.把匿名函数结尾加()小括号,是直接执行匿名函数
  () {
    print("这是一个匿名函数,执行了");
  }();


  //3.给普通的函数结尾直接加小括号,不可以被直接执行,如下:
  show() {
    print("这是一个有名字的函数show,执行了");
    // }();
  }

  // show(); //普通函数调用
 show2(){
    print("show2执行");
  }();//普通函数不能加小括号直接调用
show2();
//4.Function类型,是函数类型,可以保存函数的变量,可以把函数名字直接赋值给Function类型的变量

  Function fn1;
  fn1 = show;//函数的名字可以直接复制给Function变量,在其他语言中,函数名字就是函数的地址
   fn1();//调用show方法
  print(fn1); //打印结果是,fn1是一个闭包:Closure
  int add2 (int a,int b){
    print("add()执行 a+b= ${a+b}");
    return a+b;
  }
  //给函数指针指定明确的类型
  int  Function  (int,int) fn3 = add2;
  //
//5.把匿名函数赋值给Function变量
  fn1 = (){
    print("这是一个匿名函数2,执行了");
  };
  fn1();//执行变量里保存的函数

  //6.把带参数的函数赋值给Function变量的调用
  show3(int a,int b){
   print("show3执行,a=$a,b=$b");
   return a+b;
  }
  int result = show3(1, 2);
  print(result);
  fn1 = show3;
  //7.Function类型变量可以像普通函数那样返回值,本质上就是在调用函数
  result = fn1(3,4);
  print(result);
}


