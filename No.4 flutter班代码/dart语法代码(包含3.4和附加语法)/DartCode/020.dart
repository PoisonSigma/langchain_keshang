main(){
  //as 类型转换
  dynamic d1 = "abc123";
  var str = d1 as String;
  int length = str.length;
  // print("length=$length");

  // int i1 = d1 as int;
  // print(i1);

  //Map是键值对,泛型第一个类型是键,key, 第二个是值,value,有点像Oc字典,也有点json
  //键值对可以是任何类型
  //int String类型
  //下面是强制给出Map的类型,那么就不能给其他类型
  var m1 =Map<int,String>();
  //通过下标[]访问和赋值,[]中是键,key
  m1[0] = "abc";
  m1[2] = "123";
  // m1["str"] = 123;//类型不匹配
  // print(m1);
  //不指定泛型,那么键值都是dynamic类型,可以接受任何类型
  var m2 = Map();
  m2[0] = 123;
  m2[1] = "xyz";
  m2["name"] = "张三";
  // print(m2);
  //读取值value

  var value = m2["name"] ;
  // print(value);
  //通过as 强制类型转换
  var value2 = m2["name"] as String ;
  // var value3 = m2["name"] as int;//运行时错误,类型不对

  //通过{}键:值对初始化 key value之间用冒号:隔开,每组key value用逗号,隔开
  //下面m3因为key value 2个键值对,都是不同的类型,所以m3的泛型是<Object, Object>
  var m3 = {
    "name":"张三",
    123:123
  };
  var m4 = {
    "name":"张三",
    "age":18
  };
  // print(m4);

  //addEntries()方法添加一组数据
  m4.addEntries(
    [
      MapEntry("no", 999),
      MapEntry("学校", "第一中学")
    ]
  );
  print(m4);
}