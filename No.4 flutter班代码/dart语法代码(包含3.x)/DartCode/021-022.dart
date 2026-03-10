main() {
  //MapEntry()创建一个键值对,用来组合Map的,一般用来组合map键值对用
  //Creates an entry with key and value.创建一个包含键和值的入口
  var mt = MapEntry("age", 18);
  // print(mt);
  //字符串拼接变量,用字符串两边加引号+$变量名,之前的打印print,就是打印了,拼接后的String
  var i1 = 100;
  String str = "'i1'=$i1";
  // print(str);

  var m1 = {"name": "张三", "age": 18};
// print(m1);
//Map.map()方法是遍历Map里面的所有键值对,每次遍历把键值分别放到(key,value)中
  //箭头函数=>相当于 { return  一行代码  }
  //被map遍历的Map不会改变,但是返回值返回给=左边接受的是新的Map
  //下面例子m2是新的Map,m1被map遍历了,但是他自己的值不变
  var m2 = m1.map((key, value) => MapEntry(
      key, "abc123")); // "name":"张三",   {"name":"abc123",  "age":"abc123"}
  // print(m1);
  // print(m2);
  var m3 = m1.map((key, value) {
    String str = "map遍历执行了:key = $key  value = $value";
    // print(str);
    return MapEntry(key, str);
  }); // "name":"张三",   {"name":"abc123",  "age":"abc123"}
  // print(m1);
  // print(m3);

  //entries.map返回一个迭代器,可以是任何类型,这样就可以把Map转换为其他类型的迭代器,再转为数组
  var m4 = {"name": "张三", "age": 18};

  var it1 = m4.entries.map((e) {
    String str = "遍历中 key=${e.key}: value=${e.value}";
    // print(str);
    return str;
  });
  // print(it1);
  var l1 = it1.toList();
  // print(l1);
  // for(var item in l1){
  //      print("item=$item");
  // }
  //List 用asMap()方法转换为Map,调用map方法
   var m5 = l1.asMap();
   // print(m5);

   var l2 = [1,2,3,4,5,"abc"];
    var l3 = l2.asMap().entries.map((e) {
     String str = "key=${e.key}: value=${e.value}";
     return str;
   }).toList();
  print("l3=$l3");
}
