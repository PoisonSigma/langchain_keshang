main(){

  // Type promotion  类型提升 ,通过判断,去掉空类型,相当于可选类型,发现是非空的以后变成普通 类型,也可以理解可选类型强制解包
  // is 判断类型,可以进行类型提升
  // 非空安全下,因为没有可选类型,只有基本类型,所以不存在类型提升的去空化.就是不存在通过判断 if(a != null ) 把String? 变成String
  // 空安全下存在可选类型,去空化之后可以方便调用基本类型的方法
  // 1.== null
  // 2.!= null
  // 3. is 某个类型
  // 4. is! 某个类型
  // 5. 强制解包后类型提升

/*
  //可选类型 == null 空安全下的类型提升
  var result = fun1IsNull(["123","456","789"]);
  // var result = fun1IsNull();
  print("result=$result");

   */
/*
//可选类型 != null 空安全下的类型提升
  var result = fun1IsNotNull(["123","456","789"]);
  // var result = fun1IsNotNull();
  // var result = makeCommand("abc");//参数没传入,就是null
  // isEmptyList([1,2,3]);
  print(result);
*/

/*
  // is 判断类型提升
  // var l1 = [1, 2,3,"a","b","c"];
  List l1;
  // List? l1;
   isList(l1);
  // print(result1);

 */

// var l1 = [1, 2,3,"a","b","c"];
//   List l1;
//   List? l1;
//    isNotList(l1);

  // With (or without) null safety:

  //强制解包下的类型提升
  String str = "abc";
  // String? str;//试验null下强制解包报错
  isFun(str);
}
// Using null safety:
/*
//可选类型 == null 空安全下的类型提升
String fun1IsNull( [List<String> l1]) { //不带?不使用空安全
  //==null 判断是否为空可以进行类型提升
  if (l1 == null) return "";
  //使用空安全以后,在if 判断=null的的下面一行可以进行类型提升
  print("arguments 类型是 ${l1.runtimeType}");
  return  l1.join(","); //join 方法是把队列的每个元素进行分割插入字符
}


 */
/*
//可选类型 != null  空安全下的类型提升
String fun1IsNotNull([List<String>? l1]) {
  //不带?不使用空安全
  //==null 判断是否为空可以进行类型提升
  if (l1 != null) {
    print("l1 类型是 ${l1.runtimeType}");
    return  l1.join(","); //join 方法是把队列的每个元素进行分割插入字符
  }

  //下面是Null类型的分流
  print("l1的类型是${l1.runtimeType}");
  return "";
}

 */



//    空安全下的类型提升
 isList(Object object) {
  /*
  如果某个控制流结构的主体只有在某个变量的is表达式为真时才执行，那么在该主体内部，变量的类型会被“提升”为测试的类型。
   */
  //is 判断类型,可以进行类型提升
  if (object is List) {
    //这里的object 在 is 判断类型的时候,为真的时候会类型提升为 List的类型
    print("object类型提升后的类型是:${object.runtimeType}");
    object.forEach((element) {print(element);});  //遍历每个元素 并且打印
  } else {
    print("object类型是:${object.runtimeType}");
  }
}


// is! 不属于某个类的类型提升

 isNotList(Object? object) {
  // Object o1 ;
  if (object is! List) {
    print("1 object类型是:${object.runtimeType}");
  }
  //下面是是List类型的分流
  print("2 object类型是:${object.runtimeType}");
  //使用空安全,下面代码运行正确,可以推断出object是List类型
  // return object.isEmpty; // 不使用空安全会编译报错,类型提升不够只能无法看出if 使用is! 之后,在后面的语句是 List类型,所以是Object类型,  Object类下没有方法isEmpty
}

isFun(String? str){
  //通过强制解包来去空化,并且调用方法,强制解包没法静态解析是否为null,只能运行的时候分析,如果是null会运行报错
    str!.length;
    print("str的类型是${str.runtimeType}");
    //
    /*
    执行过一次强制解包以后,类型已经提升成String了,不能再次强制解包
    str!;//强制解包后,类型提升,但是如果强制解包null会运行报错
     */
    print("str的类型是${str.runtimeType}");
     str.length;
}

