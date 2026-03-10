main(){
  // ? 问号可选类型,可空类型
  int? i1 = 100;
  // i1 = null; //null代表空
  // print(i1);
  //如果可选类型没有赋值初始值,那么默认值是null
  int? i2;
  // print(i2);

  String? str;
  str = "abc";
  // print("=========");
  // print(str);
  // print("=========");
  // String.isEmpty 是判断是否是空白字符串,他并不是null,不是空,依然有值,只不过值是空白字符串""
  //判断是否为空白字符串,不是null,而是""空白字符串,返回true false
  //isNotEmpty跟isEmpty完全相反
  bool r1 = str.isEmpty;
   r1 = str.isNotEmpty;
  print(r1);
}