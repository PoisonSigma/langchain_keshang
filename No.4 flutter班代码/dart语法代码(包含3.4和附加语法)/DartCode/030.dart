main(){
  //转换类型parse
  String str = "123";
  int i = int.parse(str);
  // print(i);
  double f = double.parse("123.4");
  // print(f);
  //radix可以当做进制来使用,比如2进制的1000就是10进制的8, 1000 = 2的3次方=8 , 1010 = 10, 2的3次方=8 + 2的1次方
  i = int.parse("10",radix: 8);
  // print(i);
  //转换错误,程序会崩溃

/*
  try {
    i = int.parse("123.4");
  }catch(e){
    print("e=$e");
  }


  print("end");

 */
//int或者double使用toString()转换成String
str = i.toString();

str = f.toString();

str = 123.toString();

str = 123.4.toString();

print(str);
}