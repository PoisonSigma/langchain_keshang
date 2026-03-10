main() {
  Map<String, int> hist = {"a": 23, "b": 100};
  /*
  Map<String, int> hist = {"a": 23, "b": 100};
  for( var item in hist.entries){
          print("item = $item");
          print("item.key = ${item.key} item.value = ${item.value} ");
          // item.key;
          // item.value;
  }

   */
  /*
   var m1 = MapEntry("zhang3",18);
    // var  MapEntry(key:key,value:value)  = MapEntry("zhang3",18);
  var  MapEntry(:key,:value)  = MapEntry("zhang3",18);//getter和变量同名可以省略
  print("key = $key value = $value");
  // m1.key;
  // m1.value;
  // MapEntry本身也是一个class,里面有2个成员key ,value,系统有隐式getter
  //通过getter给他进行解构
  for(var MapEntry(:key,:value)    in hist.entries){
    print("key = $key value = $value");
  }

   */
  //模式验证JSON,这个json是个Map,类型是Map<String, List<Object>>
  var json = {
    'user':['zhang3',999],
    'user2':['li4',30],
  };
   var {  'user':[name,age] ,  'user2':[name2,age2] } = json;
   print("name = $name age = $age name2 = $name2 age2 = $age2");



  // print(json.length);
   /*
  if (json is Map<String, Object?> &&
      json.length == 1 &&
      json.containsKey('user')) {
    var user = json['user'];
    if (user is List<Object> &&
        user.length == 2 &&
        user[0] is String &&
        user[1] is int) {
      var name = user[0] as String;
      var age = user[1] as int;
      print('User $name is $age years old.');
    }
  }
    */


}
