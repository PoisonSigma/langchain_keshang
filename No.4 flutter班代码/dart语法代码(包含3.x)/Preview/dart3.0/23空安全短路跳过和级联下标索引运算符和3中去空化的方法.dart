main(){
  //复习之前内容:?.是只有不为null时候才执行右边的代码
  //这段代码演示 连续使用?.的 short-circuiting"短路跳过",当发现左边运算结果为null之后,右边就不再继续运算了
  //连续2个 ?.的时候编译器会有警告.原理就是上面你说的,如果第一个?.之后,发现返回了null,就直接跳过代码不继续执行了
  // 使用空安全:
  // String? notAString = null;
  String? notAString = "1234";
  fun1(notAString);

}



fun1(String? notAString) {
  var result = notAString?.length;
  //这里result = null
  result?.isEven; //isEven是返回整数的位数是奇数的时候返回true 偶数返回false
  //下面编译器警告提示:The receiver can't be null because of short-circuiting, so the null-aware operator '?.' can't be used.由于短路，接收器不能为空，因此空感知运算符` ?“不能用。
  notAString?.length?.isEven; //把上面连续2个表达式连在一起应该出现2个?.,但是编译器提示第二个应该删掉
  //上面拆开的时候是需要2个?.因为每个都可能是null
  //下面连用的时候编译器提示只用一个?. 因为最左边的notAString?.length出现?.之后如果返回了null,就不继续向右执行了,所以要执行.isEven左边的一定是非空值
  // 当方法链中使用空安全运算符时，如果接收器计算为 null，则整个方法链的剩余部分都将被短路并跳过。
  // 所以右边的.isEven没有报错,因为跳过没有执行
  notAString?.length.isEven;
  print(notAString?.length.isEven);

  // 使用空安全:

// 空安全级联,只需要用一个?..后面的级联都是用..,跟上面一样,如果发现对象为null,就短路跳过,不向下执行,所以后面的都不用继续?..
  var a1 = fun2();
   var result2 = a1
    ?..a1()
   //这里打断点 ctr+shift +d  再按 F8但不调试打断点演示,如果是 a1 = null那么就不再执行级联里面的操作
    ..a2(); //报错,尝试将“?..”运算符移动到序列中的第一个级联运算符位置。
  // List? l1 = [1,2,3,4];
  List? l1;
  funList(l1);

   // var str = toUpper(null);
  var str = toUpper("abc");
   // print("str = $str");
}
//使用3种方法去空化去空化
//1.as强制转换
// 2 ?. 当只有不空的时候才运行,空的话不执行
// 3.强制解包!.

String toUpper(  String? str) {
  return (str as String).toUpperCase();;//利用as 强制转换成String,但是如果是null,会报错
  // return '${str?.toUpperCase()}';//遇到null,就返回null,这里把null转化成String  null
  // return ' ${str !.toUpperCase()}';  //强制解包,强制去除可空的  ,遇到null直接报错
}

A? fun2(){

    return A();
}
funList(List? l1){
  // 空安全索引运算符,下标运算符?[]
   print(l1?[3]);
}

//测试  ?.. 级联用的 类A
class A{
  a1(){
    print("a1()");
  }
  a2(){
    print("a2()");
  }
}

