
main() {
  /*
  //1.不能将动态列表用作类型化列表。
  // List<int>list1 = <dynamic>[];//错误,不能用动态列表初始化,类型化的列表
  List<dynamic> list2 = <dynamic>[]; //正确
  var list3 = <dynamic>[];
   */

  // 2.as 静态分析正确,运行时检查错误
  List<Object> list1 = <String>["abc","bcd"];//正确
  // list1.add(1);//运行时候检查错误
  // List<int>list2 = list1  as List<int>;//静态分析正确,运行时检查错误无法从List<String> 转换到List<int>

  //3.<dynamic>类型注释传入到函数中的List<int>指定类型中的错误例子
  printInts([1,2,3]);//正确,List<int>
  List<dynamic> list3 = ["abc","bcd"];
  // printInts(list3); //静态分析失败,类型不匹配,List<dynamic> 不能 穿给 List<int>
  //var final等类型推断不会因为后续的赋值而改变,只在初始化的时候推断类型,下节课专门讲

  //4.没有提供足够信息的时候,会推断成dynamic
  final list = [];//没有为分析器提供足够的信息，使其无法推断出比 dynamic 更具体的类型参数
  list.add(1);
  list.add(2);
  list.add("abc");
  // printInts(list);//静态分析错误,类型不匹配,List<dynamic> 不能 穿给 List<int>

}
printInts(List <int> i)=>print(i);
