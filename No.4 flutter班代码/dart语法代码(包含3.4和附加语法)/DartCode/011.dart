main() {
  /*
  //泛型
  List<int> l0a = [];

  l0a.add(123);
  l0a.add(456);
  l0a.add(456);
  l0a.add(12);
  print(l0a);

  //判断长度  length
  print(l0a.length);

  var l0b = [];

  l0b.add(1);
  l0b.add("abc");
  print(l0b);

  var l0c = <dynamic>[];
  //List<dynamic> l0b
  //List<dynamic> l0c

  var l0d = <int>[];
  l0d.add(123);
  // l0d.add("123");

  List<int> l0e = <int>[1, 2, 3];
  print("l0e=$l0e");
  var l0f = [1, 2, 3, "xyz"];
  l0f.add(456);
  l0f.add("xyz");

  var l0g = <String>["123","xfasdf"];
  print(l0g);

  //addAll方法,批量添加
  var l0h1 = [1,2,3,"xyz"];
  var l0h2 = [4,5,6];
  var l0h3 = ["123","xyz"];
  l0h1.addAll(l0h2);
  print(l0h1);
  l0h1.addAll(l0h3);

  //insert插入,参数一是序列,从0开始
  var l2 = [1, 2, 3, 4, 5];
  l2.insert(4, 999);
  print(l2);
  //insertAll批量插入,参数1是插入位置,参数而是被插入的数组
  var l3 = [1,2,3,4,5];
  var l3b = [999,888,777];
  l3.insertAll(2, l3b);
  print(l3);

  //remove删除指定的值
  var l4 =  [1,2,3,4,5];
  l4.remove(3);
  l4.remove(5);
  print(l4);
  //removeAt
  var l5 =   [1,2,3,4,5];
  l5.removeAt(3);
  print(l5);

  //removeRange,参数1,开始删除的序列,参数2,直到删除到参数2的前一个序列
  var l6 = [1,2,3,4,5];
  l6.removeRange(0, 2);
  print(l6);
  l6.removeRange(1, 2);
  print(l6);


  //删掉最后一个
  var l7 = [1,2,3,4,5];
  l7.removeLast();
  l7.removeLast();
  l7.removeLast();
  l7.removeLast();
  print(l7);

  //isEmpty判断是否为空
  //isNotEmpty判断是否不为空
  var l8 = [];
  print(l8.isEmpty);
  print(l8.isNotEmpty);

  //reversed
  //迭代操作,先记住
  var l9 = [1,2,3,4,5];
  print(l9);
  var l9b = l9.reversed;
  print(l9b);
  var l9c = l9b.toList();
  print(l9c);
  var l9d = l9.reversed.toList();


  //map方法,等我们讲完匿名函数和箭头函数会对map后面的(){}这种匿名函数更加理解,现在只需要记住这种固定格式,这个List.map之所以放在这里,是为了大家以后复习或者查找list方法的时候可以直接在这里找到
  //List.map()方法,映射, ()括号里面的参数,是每次遍历数组里的元素,而右边的 =>箭头符号 右边的表达式是 一个闭包的缩写方法: 意思是return e+1
  //注意map()方法返回的也是一个迭代器操作Iterable,要把他存到新的list中要使用toList()方法

  var l10 = [1, 2, 3];
  // var l11 = l10.map((e) => e+1).toList();
  //遍历
  //  var l10b = l10.map((e) {
  //   return e + 1;
  // });
  var l10b = l10.map((e) =>  e+1);
   print(l10b);
   var l11  = l10b.toList();
  // (2,3,4)
  print(l11);

  // var l11 = [2,3,4];
*/
  var l12 = [1, 2, 3];
  var l13 = l12.map((e) {
    print("l12的map执行了");
    return e + 1;
  }).toList();


  // print(l14);



}
