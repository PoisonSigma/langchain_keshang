main() {
  //toInt()使用
  int f = 2.5.toInt();

  print(f);
  int f2 = (5 / 2).toInt();
  print(f2);
  // int f3 = 5/2.toInt(); 编译会报错,需要加括号修改运算优先级

  //toDouble()使用
  double f3 = f2.toDouble();
  print(f3);
}
