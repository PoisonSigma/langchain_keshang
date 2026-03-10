main(){

   //String 的contains方法,判断字符串是否包含某个字符串,返回bool类型
  String str = "张三100分";
   var r = str.contains("张三");//true,包含
   // print(r);
   r = str.contains("王五");//false不包含
  // print(r);

  // Iterbale.where只有在匿名函数中返回true的值才会被筛选,返回false不会,被筛选,返回的是Iterable
  Iterable it1 = [1,2,3,4,5];
  //Iterbale.where
  var it2 = it1.where((element) => element%2 == 0);
  print(it2);
  //List.where
  var l1 = [1,2,3,4,5,6];
  var it3 = l1.where((element) => element%2 == 0);
  print(it3);

  //生成0-19
  var l2 = List.generate(20, (index) => index);
  print(l2);
  //获取5的倍数
  var l3 = l2.where((element) => element%5 == 0).toList();
  print(l3);

  //Map.entries.map 返回的也是Iterbale,所以也可以使用.where
  var m1 = {
    "张三":100,
    "李四":60,
    "王五":59
  };
  var it4 = m1.entries.map((e){
    var str = "${e.key} ${e.value}分";
    return str;
  });
  for(var item in it4){
       print("item=$item");
  }
  //获取包含张三的元素,查看张三的成绩
  var it5 = it4.where((element) => element.contains("张三"));
  print(it5);


}