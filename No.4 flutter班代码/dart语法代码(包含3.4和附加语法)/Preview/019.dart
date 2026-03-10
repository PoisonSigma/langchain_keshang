main() {
  //1.Set是集合,标准写法 new Set<泛型>()
  Set<int>s1 = new Set<int>();
  //2.通常我们用var来定义s1,因为等号右边有完整类型,左边可以少写几个字母,
  var s2 = new Set<int>();
  s2.add(2);
  s2.add(1);
  s2.add(1); //加入2个1,但是集合中只有一个1
  print(s2); //可以看到只有1个1,不会重复
  //3.Set没有顺序,不能通过下标访问:
  //  s2[0] = 3;
  //4.其中new 和泛型都可以省略
  var s3 = Set(); //如果不写泛型,那么就是dynamic,可以接受任意类型
  s3.add(1);
  s3.add("str");
  print(s3);
  //5.Set.from(数组)可以用一个数组初始化Set
  var s4 = Set.from([1,2,3,4,5]);
  print(s4);
  //5.1可以用另一个Set初始化Set
  var s4b = Set.from(s3);
  print("s4b = $s4b");
  //6.for in遍历Set集合
  for(var item in s4){
       print("item=$item");
  }
  for(var item in s3){
    print("item=$item");
  }
  //7.Set不可以重复
  var s5 = Set.from([1,2,3]);
  s5.add(1);
  s5.add(1);
  print(s5);
}
