main(){

  //简单的数学运算
  int a = 3 + 5;
  print(a);
  int b = a - 3;
  print(b);
  int c = 3 * 3;
  print(c);
  // int d = 5/2;//错误, 右边的值是2.5是一个double 无法复制给左边的 int类型
  //int d = 2.5;上面的内容相当于这个,把double赋值给了int
  //很多时候不知道计算结果到底是整数还是浮点数,那么可以通过toInt来强制之把结果变成int,这就是为什么先讲类型转换再讲数学运算符
  int d = (5/2).toInt();//把2.5从double转换为int赋值给左边
  print(d);
  double e = 5 / 2;

  print(e);



  int f = 5%2;  //5除以2 = 2余数是1
  print(f);
  int g = 10%2; //10除以2可以整除,余数是0
  print(g);
}