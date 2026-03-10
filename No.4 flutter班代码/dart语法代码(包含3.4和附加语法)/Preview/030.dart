main(){
   //转换类型parse
  String str = "123";
  int i = int.parse(str);
  print(i);
  str = "123.4";
  double f = double.parse(str);
  print(f);
  //转换错误,程序会崩溃
  // i = int.parse("123.4");//运行报错,因为str这时候有小数点了,要用double.parse
  // i = int.parse("abc");//报错

  //使用try catch捕获异常
  try{
    i = int.parse("abc");
  }catch(e){
    print("转换错误");
  }
  print("end");

  //int或者double使用toString()转换成String
  i = 123;
  str = i.toString();
  print(str);
  str = f.toString();
  print(str);

  str = 123.toString();//可以直接字面量.toString
  print(str);
  str = 123.4.toString();
  print(str);

}