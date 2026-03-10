main() {
  //Iterable的定义
  var l1 = [1, 2, 3, 4, 5];
  List l2 = [1, 2, 3, 4, 5];
  Iterable it1 = [11, 22, 33, 44, 55];
  // abstract class List<E> implements EfficientLengthIterable<E>
  // abstract class EfficientLengthIterable<T> extends Iterable<T>
  //下面补充两个关于继承的概念,因为类的继承我们还没有讲,只需要理解,子类中会有父类的方法,List中的方法父类Iterable中也有就行了
  //implements 也是继承,是可以继承多个父类,并且必须继承父类中所有的抽象方法和普通方法,这种概念,在其他语言中也可以叫做继承多个接口interface,或者遵守多个协议protocol,可以理解为,一个类可以同时继承多个类
  //extends继承,只能继承1个父类,里面的抽象方法必须实现,普通方法可以不用实现.
  // l1.forEach((element) {print("l1 遍历 $element");});
  it1.forEach((element) {
    // print("it1 遍历 $element");
  });

  // Set.from方法()初始化的时候要一个Iterable,这时候我们给[1,2,3,4,5],这种方括号的字面量,或者Iterable或者List都可以
  var s1 = Set.from([1,2,3,4,5]);
  // print(s1);
  var s2 = Set.from(l2);
  // print(s2);
  var s3 = Set.from(it1);
  // print(s3);
//通过上节课学到的is运算符 判断List是Iterable的子类
   if(l1 is Iterable){
     // print("真");
   }
   //Map不是Iterable的子类
  Map m1 = {"name": "张三", "age": 18};
  var itm1 = m1.entries.map((e) => print("Map m1遍历了"));
  // print(itm1);

  m1.forEach((key, value) {print("");});
  if(m1 is Iterable){
    print("真");
  }
  // print(l1.first);
  // print(l1.last);
  // print(it1.first);
  // print(it1.last);
  /// As long as the returned [Iterable] is not iterated over,
  /// the supplied function [test] will not be invoked.
  ///只要返回的[Iterable]没有被遍历，
  ///提供的函数[test]将不会被调用。
  l1.map((e) => print("遍历123 $e")).toList();
  it1.map((e) => print("遍历iterable123")).toList();
  // print(l1);
  // print(it1);
}
