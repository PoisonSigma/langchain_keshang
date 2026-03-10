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


  //1. 可选类型 == null 空安全下的类型提升
  // funIsNull();
  // var l1 = [1,2,3,"a","b","c"];
  // funIsNull(l1);

  /*
  //2. 可选类型 != null  空安全下的类型提升

  funIsNotNull();
  // var l1 = [1,2,3,"a","b","c"];
  // funIsNotNull(l1);

   */
  /*
  //3. is 判断类型提升

  // isList();
  isList([1,2,3,4,"a"]);
   */
  // 4. is! 某个类型
  // isNotList();
  // isNotList([1,2,3,4,"a"]);
  //5. ! 强制解包之后的类型提升
  isFun("abc");
}
/*
//可选类型 == null 空安全下的类型提升
funIsNull([List<Object>? l1 ]){
      if(l1 == null){
        print("null");
        print("l1的类型是 ${l1.runtimeType}");
        return;
      }
      print("l1的类型是 ${l1.runtimeType}");
      l1.length;
}

 */
/*
funIsNotNull([List<Object>? l1 ]){
  if(l1 != null){
    print("l1的类型是 ${l1.runtimeType}");
    l1.length;
    return;
  }
  //== null 的分流
  print("l1的类型是 ${l1.runtimeType}");
}
 */
/*
isList([Object? object]){
    if(object is List){
      print("object 的类型是 ${object.runtimeType}");
      object.forEach((element) {
        print(element);
      });
    }
    print("object 的类型是 ${object.runtimeType}");
}

 */

/*
isNotList([Object object]) {
  // Object o1 ;
  if (object is! List) {
    print("1 object类型是:${object.runtimeType}");
  }else{
    // object.length; //空安全下,可以把Ojbect类型静态分析成 真实的List类型
    print("2 object类型是:${object.runtimeType}");
  }
  //下面是是List类型的分流



  //使用空安全,下面代码运行正确,可以推断出object是List类型
  // return object.isEmpty; // 不使用空安全会编译报错,类型提升不够只能无法看出if 使用is! 之后,在后面的语句是 List类型,所以是Object类型,  Object类下没有方法isEmpty
}

 */

isFun(String? str){
  /*
  print("str的类型是${str.runtimeType}");
  str!.length;
      print("str的类型是${str.runtimeType}");
      str!.length;
      print("str的类型是${str.runtimeType}");
*/
  str!;
  str.length;
  print("str的类型是${str.runtimeType}");
}