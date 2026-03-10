main() {
  //MapEntry()创建一个键值对,用来组合Map的,一般用来组合map键值对用
  //Creates an entry with key and value.创建一个包含键和值的入口
  var mt = MapEntry("xxx", "abc");
  // print(mt);
  //字符串拼接变量,用字符串两边加引号+$变量名,之前的打印print,就是打印了,拼接后的String
  int i = 100;
  String str1 = "遍历里面执行的新的value=$i";
  print(str1);
  var m1 = {"name": "张三", "age": 18};
  // print(m1);
  //.map()方法是遍历Map里面的所有键值对,每次遍历把键值分别放到(key,value)中
  //箭头函数=>相当于 { return  一行代码  }
  //被map遍历的Map不会改变,但是返回值返回给=左边接受的是新的Map
  //下面例子m2是新的Map,m1被map遍历了,但是他自己的值不变
  var m2 = m1.map((key, value) => MapEntry("abc", "123"));
  print("m1=$m1");
  print("m2=$m2");

  //下面你是不用箭头函数的map,因为要在{}里面不只一行代码
  //
  var m3 = m1.map((key, value) {
    //字符串拼接变量,用字符串两边加引号+$变量名,跟打印一样
    String str = "遍历里面执行的新的value=$value";
    print("str=$str");
    return MapEntry(key, str);
  });

  print("m3=$m3");


  var m4 = {"name": "张三", "age": 18};
  var m5 = m4.entries.map((e) {
    String str = "${e.key} : ${e.value}";
    return str;
  });
  //这里返回一个Iterable迭代器,打印出来是小括号,之前讲过的List.map也是返回的Iterable迭代器,打印出来是小括号
  //查看011.dart里面的l14.map()返回的是Iterable
  print("m5=$m5");
  var l1 = m5.toList();
  print("l1=$l1");

  //List 用asMap()方法转换为Map,调用map方法
  List l2 = ["abc", "xyz"];
  var m6 = l2.asMap();
  var it2 = m6.entries.map((e) {
    String str = "${e.key} : ${e.value}";
    return str;
  });
  print(it2);
  var l3 = it2.toList();
  print(l3);
}
