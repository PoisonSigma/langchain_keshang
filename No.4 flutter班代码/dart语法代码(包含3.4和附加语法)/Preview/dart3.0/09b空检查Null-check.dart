main(){

  // 空检查（Null-check）
  // 格式: 子模式? ,例如:switch 中的 {case var s?  ..}
  // 空检查模式首先匹配值是否不为null，然后使用相同的值匹配内部模式。它们允许您绑定一个变量，该变量的类型是可匹配的可空值的非空基础类型。
  //上面内容有点拗口,意思就是,空检查可以把传进来的可空的类型的String?  用一个 String的非空类型去接受 ,如果String?里面存的值是null,那么匹配失败,向下流转
  // 空检查的作用是,遇到null 值视为匹配失败而不抛出异常，遇到非空的就接受并且绑定非空值

  String? str = 'abc';
  // String? str = null;


/*
  //注意,如果str有了确定的值,那么编译器会认为他的类型就不在是String?,而是String .
  //Warning: The null-check pattern will have no effect because the matched type isn't nullable.
  // 警告:空检查模式将不起作用，因为匹配的类型不是可空的
  //解决方法把下面的switch语句放到函数中
  switch (str) {
    case var s?:
      print("非空字符串 $s");
  // 's' 在这里具有非空字符串类型。
    case null:
      print("空字符串2");
  }

 */
checkNull(str);
}

checkNull(String? str){
  // String str2 = str!;//直接会报错,异常
  print("进入函数");
  switch (str) {
    case var s?:  // 这个是空检查,  s?的特点是,只有非空的才会匹配,如果是null就不匹配,匹配失败,可以把case null常量模式放到下面去接收,防止漏掉null
    // case var s://这个不带问号的s,是全匹配,不管是不是空,这样下面的case null就会失效
      print("匹配到非空字符串 s= $s");
      print("s的类型是:${s.runtimeType}"); //可以吧
      // String str2 = s!;//这里面没用到空检查,所以使用s给String赋值,需要强制解包.如果s为抛出异常
      String str3 = s;//这里试验使用空检查,s本身就是非空的String,如果遇到str=null,这行不会被执行,因为没有匹配到
    // 's' 在这里具有非空字符串类型。
    case null:  //这个是常量模式,后面会讲  因为上面空字符串会被上面的空检查匹配失败,所以用这个常量模式null去匹配null,防止匹配不到null
      print("匹配到null");
  }
}