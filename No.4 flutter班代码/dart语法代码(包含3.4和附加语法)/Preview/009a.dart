main() {

  //toInt()使用
  int f = 2.5.toInt(); //把double转换为int,并且赋值给左边 ,把2.5后面的小数点去掉,只留下整数部分
  //额外补充一下,计算机中存储小数点的数字,是float,内存中的样子不是传统的整形数字,内存中可以看到2.5不是存了2.5,而是一大串东西
  print(f);
  //toDouble()使用

  // double f2 = f;//报错,因为f是int类型,不能赋值给double
  double f3 = f.toDouble();

  print(f3);

}
