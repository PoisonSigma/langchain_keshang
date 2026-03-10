main() {
  /*
函数:是可以重复执行的代码段
函数定义的格式:
返回类型 函数名(参数列表){
函数体
return 返回值
}
 */
  // int a = 3;
  // int b = 4;
  // fun1(a, b);
  // fun2();
  // fun3();

  int a = fun4();
  // print(a);
  // int b = fun5();
  // fun5();
  // print(a);
  fun6();
}

dynamic fun3(){
  return 3;
}
int fun1(int a, int b) {
  print("fun1执行");
  print("fun1执行2");
  print("fun1执行3");
  print("=======");
  return a + b;
}

fun2() {
  print("fun2()");
}
// dynamic fun3(){
//   print("fun3()");
// }
dynamic fun4(){
  print("fun4");
  return 1;
}
fun5(){
  print("fun5");
}

void fun6(){
  print("fun6");
  // return 1;
}