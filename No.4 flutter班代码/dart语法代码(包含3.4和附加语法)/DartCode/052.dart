//dynamic类型是自动把2个变量按照实际传入的值,自动识别出2个类型,2个类型可以不同
//runtimeType变量的运行时类型
// String getStr1(dynamic row, dynamic line) {
//   print("row的类型是${row.runtimeType}");
//   print("line的类型是${line.runtimeType}");
//   return "位置是第$row行 第$line 列";
// }

//在功能上,上面和下面的方法功能上是一样的 ,跟上面的dynamic类型功能一样,但是泛型语法出现更早
//泛型的格式是<>尖括号里面放着类型
// 方法的()小括号前面加<>尖括号,里面是类型
//下面方法只给了一个泛型T,那么T的类型只能是一种,如果  row和line都用了一个T,那么如果传入的只都是int,T的类型就是int,如果传入了不同的类型,会变成Object
String getStr2<T>(T row, T line) {
  print("T=$T");
  return "位置是第$row行 第$line 列";
}
//允许使用多个泛型
String getStr3<T1,T2>(T1 row, T2 line) {
  print("T1=$T1");
  print("T2=$T2");
  return "位置是第$row行 第$line 列";
}
main() {
  var str;
  // str = getStr1(3, 3);
  // str = getStr1(3.0, 3);

  // List<int> l1 = [1,2,3,4,5];
  // 显示的在<>尖括号中指定类型,那么后面传入参数也要是这种类型
  // str = getStr2<int>(3, 6);
  // str = getStr2<int>(3, 6.0);//报错,指定了泛型的类型是int,但是传入的参数里有double
  // str = getStr2<double>(3, 6);
  // str = getStr2<Object>(3, "123abc=====");

  //下面没有在<>尖括号中指定类型,那么函数根据参数的实际类型自动变成这个类型
  // str = getStr2(3, "123abc=====");
  // str = getStr2(3, 3);
  str = getStr3("abc", 3.14);
  print(str);
}
