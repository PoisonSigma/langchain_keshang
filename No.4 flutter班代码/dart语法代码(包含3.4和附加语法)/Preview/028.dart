main(){
  // ? 问号可选类型,可空类型
  int? i1 = 100;
  i1 = null;

  print("i1=$i1");

  //如果可选类型没有赋值初始值,那么默认值是null
  String? str;
  print(str);
  str = "";
  print(str);
  print("一条横线====");

  if(str == null ){
    print("str = null");
  }else{
    print("str不等于null =$str|");
  }
  // String.isEmpty 是判断是否是空白字符串,他并不是null,不是空,依然有值,只不过值是空白字符串""
  //判断是否为空白字符串,不是null,而是""空白字符串,返回true false
  //isNotEmpty跟isEmpty完全相反
  var r2 = str.isEmpty;
  print(r2);
  r2 = str.isNotEmpty;
  print(r2);

}