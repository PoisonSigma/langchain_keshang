main(){
  // 空检查（Null-check）
  // 格式: 子模式? ,例如:switch 中的 {case var s?  ..}
  // 空检查模式首先匹配值是否不为null，然后使用相同的值匹配内部模式。它们允许您绑定一个变量，该变量的类型是可匹配的可空值的非空基础类型。
  //上面内容有点拗口,意思就是,空检查可以把传进来的可空的类型的String?  用一个 String的非空类型去接受 ,如果String?里面存的值是null,那么匹配失败,向下流转
  // 空检查的作用是,遇到null 值视为匹配失败而不抛出异常，遇到非空的就接受并且绑定非空值
  String? str = "abc";
  // String? str = null;
  /*
  switch(str){
    case var s?:// 这个是空检查,  s?的特点是,只有非空的才会匹配,如果是null就不匹配,匹配失败,可以把case null常量模式放到下面去接收,防止漏掉null
    // case var s:
      String str2 = s;//空检查作用:去掉null,如果是null,这行case匹配失败.
      print("s= $s");
      print("str2 = $str2");
      print("${s.runtimeType}  ${str2.runtimeType} ");
    case null:
      print("null adsasfadsf");
  }

   */
  nullCheck(str);
}
nullCheck(String? str){
  // String str2 = str!;
  // String str2 = str;
  switch(str){

    case var s?:// 这个是空检查,  s?的特点是,只有非空的才会匹配,如果是null就不匹配,匹配失败,可以把case null常量模式放到下面去接收,防止漏掉null
    // case var s:
  String str2 = s;//空检查作用:去掉null,如果是null,这行case匹配失败.
      print("s= $s");
      print("str2 = $str2");
      print("${s.runtimeType}  ${str2.runtimeType} ");


    case null:
      print("null");
  }
}