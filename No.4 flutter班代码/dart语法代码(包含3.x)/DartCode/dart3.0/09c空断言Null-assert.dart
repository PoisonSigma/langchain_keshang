main(){
  //空断言Null-assert
//格式  子模式!
//空断言模式可以匹配空和非空,非空就接受非空值,并且是去掉?问号的非空类型,如果是null,就抛出异常
//使用空断言模式进行匹配作用:为了确保 null 值不会被匹配失败,空检查,如果遇到null,会不匹配,case向下运行,但是空断言不会,空的也会匹配,但是会抛出异常
//   assert(1>3,"描述信息");
/*
  // String? str = "zhang3";
  String? str = null;
  nullAssert(str);
}
nullAssert(String? str){
 // String str2 = str!;
  try {
    switch (str) {
      case var s!:
        String str2 = s;
        print("str2 = $str2");
        print("${s.runtimeType}  ${str2.runtimeType} ");
    }
  }catch(e){
    print("e = $e");
  }

 */
  //使用空断言模式,从变量声明模式中消除 null 值，
  (int?,int?)position = (100,200);
  // position = (null,300);
  print(position.runtimeType);
  // var (x as int,y as int) = position;//强制类型转换方法确定类型
  var (x!,y!) = position;
  // x = null;
  print(x.runtimeType);
  print(y.runtimeType);
}