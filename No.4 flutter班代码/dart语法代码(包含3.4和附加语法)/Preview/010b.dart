main(){
  fun1();//
  fun1();
  fun1();
  fun2();
print("xxxxxx");
  int a =  fun3();
  // double b = fun3();//编译不报错,运行报错,因为fun3返回的是int不是double,运行时发现函数fun3实际返回值是int类型
   int r1 = add(3,4);
   int r2 = add(10, 10);
  // double c = fun2();//运行错误,fun2()因为没有返回任何值,函数的返回值是Null,不是double, type 'Null' is not a subtype of type 'double'
   show("老五");
   print(add(5, 5));
}
/*
函数:是可以重复执行的代码段
函数定义的格式:
返回类型 函数名(参数列表){
函数体
return 返回值
}
 */
//fun1这两个是等价的,如果不写函数类型,就默认是dynamic返回类型
fun1(){
  print("1+1=2");
  print("2+2=4");
  print("=====");
}
dynamic fun2(){
  print("1+1=2");
  print("2+2=4");
  print("=====");
}
//void是空的意思,指函数不能返回任何值

dynamic fun3(){
  return 3;
}

void fun4(){
  // return 2;//如果返回就会报错
}

//dynamic区别于var的是:var不能用作函数返回类型
//错误,var不能用来作为函数的返回类型使用
/*
var fun3(){
print("fun1");
}
 */

//函数参数列表
void show(String str){
   print("show执行str=$str");
}
int add(int a,int b){
   return a+b;
}
