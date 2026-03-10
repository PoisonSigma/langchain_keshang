main() {
  //复习之前内容:?.是只有不为null时候才执行右边的代码
  //这段代码演示 连续使用?.的 short-circuiting"短路跳过",当发现左边运算结果为null之后,右边就不再继续运算了
  // String? str = "abcd";
  // String? str = null;
  // fun1(str);

  // 空安全级联,只需要用一个?..后面的级联都是用..,跟上面一样,如果发现对象为null,就短路跳过,不向下执行,所以后面的都不用继续?..
  // var a = A();
  // a.a1();
  // a.a2();
  // a
  /*
    var result = A()
      ..a1();
    // ..a2();
  print("result = $result");
*/

/*
  // 空安全级联,只需要用一个?..后面的级联都是用..,跟上面一样,如果发现对象为null,就短路跳过,不向下执行,所以后面的都不用继续?..
  var a2 = fun2();
  a2
    ?..a1()
     ..a2();

 */
/*
// 空安全索引运算符,下标运算符?[]
  // List? l1 = [1,2,3,4];
  List? l1;
  fun3(l1);
 */

  //使用3种方法去空化去空化
//1.as强制转换
// 2 ?. 当只有不空的时候才运行,空的话不执行
// 3.强制解包!.
//   var result3 = toUpper(null);
  var result3 = toUpper("abc");
  print("result3=$result3");
}

fun3(List? l1) {
  print(l1?[2]);
}

A? fun2() {
  // return A();
}

String toUpper(String? str) {
  // return (str as String).toUpperCase();//利用as 强制转换成String,但是如果是null,会报错
  // return  "${str?.toUpperCase()}";//遇到null,就返回null,这里把null转化成String  null
  return str!.toUpperCase(); //强制解包,强制去除可空的  ,遇到null直接报错
}

fun1(String? str) {
  // var result = str?.length;
  // var result2 = result?.isEven;
  // print("result2 = $result2");
  var result3 = str?.length.isEven; //编译器警告
  //连续2个 ?.的时候编译器会有警告.原理就是上面你说的,如果第一个?.之后,发现返回了null,就直接跳过代码不继续执行了
  print("result3 = $result3");
}

//测试  ?.. 级联用的 类A
class A {
  a1() {
    print("a1()");
  }

  a2() {
    print("a2()");
  }
}
