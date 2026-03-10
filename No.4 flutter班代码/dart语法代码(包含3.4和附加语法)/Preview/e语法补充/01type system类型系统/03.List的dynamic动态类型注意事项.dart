/*
//1.不能将动态列表用作类型化列表。


main(){
    // List<int> list = <dynamic>[];//错误,不能用动态列表初始化,类型化的列表
  List<dynamic> list2 = <dynamic>[];//正确
  var list3 = <dynamic>[];//正确
}

 */
/*
2.as 静态分析正确,运行时检查错误

main(){
    List<Object> list = <String>["abc","bcd"];//左右都有类型注释,可以赋值
    list.add(1);
  List<int> list2 = list as List<int>; //静态分析正确,运行时检查错误无法从List<String> 转换到List<int>
}
 */


/*
//3.<dynamic>类型注释传入到函数中的List<int>指定类型中的错误例子
静态分析：失败
void printInts(List<int> a) => print(a);//printInts() 函数期望参数类型为 List<int>，导致类型不匹配

void main() {
  //var final等类型推断不会因为后续的赋值而改变,只在初始化的时候推断类型,下节课专门讲
  final list = [];//没有为分析器提供足够的信息，使其无法推断出比 dynamic 更具体的类型参数
  list.add(1);//var final等类型推断不会因为后续的赋值而改变,只在初始化的时候推断类型
  list.add(2);//虽然只添加了2个int整形,但是list还是dynamic类型
  // printInts(list);//The argument type 'List<dynamic>' can't be assigned to the parameter type 'List<int>'.
  //参数类型` List<dynamic> `不能被赋值给参数类型` List<int> `。
  // 是因为初始化声明 var list = [] 没有为分析器提供足够的信息，使其无法推断出比 dynamic 更具体的类型参数。printInts() 函数期望参数类型为 List<int>，导致类型不匹配。
}
 */





//静态分析正确的例子:list 的类型有了明确的类型注释(泛型类型  是 <int>) 跟 printInts的形参类型一样
void printInts(List<int> a) => print(a);//printInts() 函数期望参数类型为 List<int>，导致类型不匹配

void main() {
  final list = <int> [];//在创建列表时添加类型注解<int> ,这时候调用printInts成功
  list.add(1);
  // list.add("abc");//这里不能在add  "abc",必须给int类型
  printInts(list);
}

