main(){
    Map<String, int>hist={
      "a":23,
      "b":100
    };
    for(var item in hist.entries){
        print("item = $item");
        print("item.key = ${item.key}");
        print("item.value = ${item.value}");
    }
     var m1 = MapEntry("age",18);//创建,
  // MapEntry本身也是一个class,里面有2个成员key ,value,系统有隐式getter
  //通过getter给他进行解构
   var MapEntry(key:key,value:value) = m1;
   print("key = $key value = $value");

   for (var MapEntry(:key,:value) in hist.entries ){
        print("key = $key value = $value");
   }

   //模式验证JSON,这个json是个Map,类型是Map<String, List<Object>>
  var json = {
     'user1':['zhang3',18],
    'user2':['li4',30],
  };
   //解构Map形式
   var {'user1':[name1,age1] ,'user2':[name2,age2]} = json;
   // print("name1 = $name1 age2 = $age2");

   //如果不用模式验证
  if(json is Map<String, List<Object>> && json.length == 2 &&
      json.containsKey('user1')) {
    print("进入判断");
    var user1 = json["user1"];
    // if (user1 is List<Object>) { //注意,如果没有这个判断,下面user1[0]编译出错
      var name = user1![0];
      //The method '[]' can't be unconditionally invoked because the receiver can be 'null'. (Documentation)  Try making the call conditional (using '?.') or adding a null check to the target ('!').
    //方法不能无条件调用,因为接受者可能是null,使用!强制解包可以运行
      var age = user1![1];
      print("name = $name");
      print("age =$age");
    // }

  }
}