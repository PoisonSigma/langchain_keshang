//全局变量定义在函数外面,他的值一直被保留
int g_i = 0;
main(){
  // fun1();
  // fun1();
  // fun2(100);
  // fun2(100);
  int i = 0;
  i = fun3(i);
  print("i=$i");
  i = fun3(i);
  print("i=$i");
  i = fun3(i);
  print("i=$i");
}
fun1(){
  g_i++;
  print("g_i=$g_i");
}

fun2(int a){//call 调用子程序 , push 到栈里面 push edx,  32位, 4个字节 esp栈顶指针寄存器 esp - 4
  int i = 0;
  i++;
  print("i=$i");
}

fun3(int i){
  // print("i=$i");
  // return i++;
  i++;
  return i;
  // return ++i;
}