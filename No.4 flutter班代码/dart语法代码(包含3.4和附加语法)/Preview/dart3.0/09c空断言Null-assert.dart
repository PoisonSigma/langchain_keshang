//空断言Null-assert
//格式  子模式!
//空断言模式可以匹配空和非空,非空就接受非空值,并且是去掉?问号的非空类型,如果是null,就抛出异常
//使用空断言模式进行匹配作用:为了确保 null 值不会被匹配失败,空检查,如果遇到null,会不匹配,case向下运行,但是空断言不会,空的也会匹配,但是会抛出异常
main() {
  // String? name = "zhang3";
  String? name = null;


  nullAssert(name);
}

nullAssert(String? str) {
  try {
    switch (str) {
      case var s!: //空断言可以接受空和非空 ,如果匹配到了null就抛出异常,把整个switch用try catch包住处理异常
        String str2 = s; //这里的s已经是非空的了.是String类型
        print("s = $s");
        print("s的类型是  ${s.runtimeType}");

      case null: //这个case不会被匹配到,因为上面的case 是空断言,空和非空都会被上面匹配到
        print("null");
    }
  }
  catch (e) {
    print("e = $e");
  }

  //使用空断言模式,从变量声明模式中消除 null 值，
  //
  (int?, int?) position = (2, 3);
  print(position.runtimeType);
  var x1 = position.$1;
  x1 = null;//x1类型是 int?可以赋值null
  print("x1类型 ${x1.runtimeType}");
  var( x!, y!) = position;
  // x = null;//报错,x是非空类型,不能赋值null
  print(x.runtimeType);
  print(y.runtimeType);

}
