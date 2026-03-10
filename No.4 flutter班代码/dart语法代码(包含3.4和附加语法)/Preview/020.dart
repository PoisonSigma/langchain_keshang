main() {
// //as 类型转换
//   dynamic d1 = "xyz12345";
//   String str = "abc";
//   print("长度是=${str.length}");
//   print("d1=$d1");
//   var d2 = d1 as String;
//   int length = d2.length;
//   print("d2的长度是$length");

  //Map是键值对,泛型第一个类型是键,key, 第二个是值,value,有点像Oc字典,也有点json
  //键值对可以是任何类型
  //int String类型
  //下面是强制给出Map的类型,那么就不能给其他类型
  var m1 = Map<int, String>();
  //通过下标[]访问和赋值,[]中是键,key
  m1[0] = "abc";
  m1[100] = "xyz";
  // m1["abc"] = "zzz"; //报错,key值不对
  print(m1);

  //不指定泛型,那么键值都是dynamic类型,可以接受任何类型
  var m2 =new Map(); //new可以省略
  m2[0] = "123xyz";
  m2[1] = 789;
  m2["name"] = "张三";
  print(m2);

  //读取值value
  var value = m2["name"];
  print("value= $value");



  var value2 = m2["name"] as String;//通过as 强制类型转换
  print("value2= $value2");
  // var value3 = m2["name"] as int;//报错,String不能转换成int
  // print("value3= $value3");

  //通过{}键:值对初始化 key value之间用冒号:隔开,每组key value用逗号,隔开
  //下面m3因为key value 2个键值对,都是不同的类型,所以m3的泛型是<Object, Object>
  var m3 = {
    "name":"张三",
    123:123
  };
  print("m3=$m3");
  //
  var m4 = {
    "name":"张三",
    "age":18
  };//这里自动推断的类型是<String, Object>,因为2个key都是String,但是2个value一个是String 一个是int

  //addEntries()方法添加一组数据
  m4.addEntries([
    MapEntry('age', 18),
    MapEntry("name", "张三"),
    // MapEntry(18, 18)//保存key是int不是String ,但是m4是<String, Object>,类型不匹配

  ]
  );


}
