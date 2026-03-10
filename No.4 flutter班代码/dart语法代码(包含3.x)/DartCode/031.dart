main() {
  //String 的contains方法,判断字符串是否包含某个字符串,返回bool类型
  String str = "张三 100分";
  var r = str.contains("张三");

  r = "李四 60分".contains("李四");
  // print(r);
  // Iterbale.where只有在匿名函数中返回true的值才会被筛选,返回false不会,被筛选,返回的是Iterable
  Iterable it1 = [1, 2, 3, 4, 5, 6];
  var it2 = it1.where((element) => element % 2 == 0); // (2,4,6 )
  var l1 = it1.where((element) => element % 2 == 0).toList(); // [2,4,6 ]
  // print(it2);
  // print(l1);

  //List.where
  var l2 = List.generate(10, (index) => index * 2);
  // print(l2);
  var it3 = l2.where((element) => element % 4 == 0); //(0,4,8,12,16)
  // print(it3);

  var it4 = Iterable.generate(20, (index) => index)
      .where((element) => element % 5 == 0); //余处
  // print(it4);

  //Map.entries.map 返回的也是Iterbale,所以也可以使用.where
  var m1 = {"张三": 100, "李四": 60, "王五": 70};
  var it5 = m1.entries.map((e) => "${e.key} ${e.value}分");
  // var me = MapEntry("zhang3",100);
  // print(me);
  // print(it5);
  for(var item in it5){
       // print("item=$item");
  }
  var l3 = it5.where((element) => element.contains("张三")).toList();
  print(l3);
}
