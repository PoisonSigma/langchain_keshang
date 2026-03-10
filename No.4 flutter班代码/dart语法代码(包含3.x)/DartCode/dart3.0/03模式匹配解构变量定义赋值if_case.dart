/*
dart3.0中引入模式Patterns [ˈpætərns]的概念
模式
版本说明：模式需要至少3.0的语言版本。

模式是Dart语言中的一种语法类别，类似于语句和表达式。模式表示一组可能匹配实际值的形状。
 */

main() {
  /*
  var l1 = [1, 2];
  // const int a = 1;
  // const int b =
  ;
  switch (l1) {
    // case [1, 2]:
    //   print("常量模式匹配");
      // break;
    //解构
  //解构Destructuring
    // case [int a,int b]:
    case [int a,int b]:
      print("解构 $a $b");
  }

   */
  // List模式[a，b，c]从numList解构出三个元素......
  /*
  var l2 = [1,2,3];
  var [a,b,_] = l2;
  print("$a $b");
*/
   //switch 的case中 可以使用逻辑运算符
  var list = ["abc",99];
  /*
  switch(list){
  //case可以通过 逻辑判断 || && 等进行判断
  //这里面case要求符合条件是, [ 第一个元素是abc或者b,第二个元素可以是任意类型,用定义的 变量c接收,
  // 这里是解构,把List里的第二个值赋值给了变量c
    case ['abc'|| "b",var c ]:
      print("匹配成功 $c");
  }*/

  //if case 是把case放在()小括号里面进行匹配,相当于单一一组的switch case,要求dart 3.0版本以上
  if(list case [String str , int b] ){
    print("str = $str , b = $b");
  }


// 声明新的变量 a、b 和 c。
  // 模式变量声明必须以 var 或 final 开头，后跟一个模式。
// final   (x2,y2) = (10,20);
//   (x2,y2) = (1,2);
//   x2 = 99;
  /*
  var (x,y) = (30,40);//这个还是定义新的变量x,y
  (x,y) = (30,40);
  print("$x $y");
  // var (y,x) = (x,y);
  print("$x $y");
  var z;
  (x,y,z) = (x,x,x);

  x = 99;
  print("$x $y $z");

   */
}
