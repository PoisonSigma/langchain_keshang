main() {
  //默认用方括号初始化一个变量,会被识别成List
  var l1 = [1, 2, 3, 4, 5];
  List l2 = [1, 2, 3, 4, 5];
  //下面补充两个关于继承的概念,因为类的继承我们还没有讲,只需要理解,子类中会有父类的方法,List中的方法父类Iterable中也有就行了
  //implements 也是继承,是可以继承多个父类,并且必须继承父类中所有的抽象方法和普通方法,这种概念,在其他语言中也可以叫做继承多个接口interface,或者遵守多个协议protocol,可以理解为,一个类可以同时继承多个类
  //extends继承,只能继承1个父类,里面的抽象方法必须实现,普通方法可以不用实现.
  //abstract class List<E> implements EfficientLengthIterable<E>        //List 遵守 EfficientLengthIterable 协议
  // abstract class EfficientLengthIterable<T> extends Iterable<T>       //EfficientLengthIterable 继承  Iterable  //所以可以理解为List是Iterable的孙子
  Iterable it1 = [1, 2, 3]; // abstract mixin class Iterable<E>/
  // List的forEach就是调用的父类Iterable的forEAch
  l1.forEach((element) {
    print(element);
  });
  it1.forEach((element) {
    print(element);
  });

  // Set.from方法()初始化的时候要一个Iterable,这时候我们给[1,2,3,4,5],这种方括号的字面量,或者Iterable或者List都可以
  var s1 = Set.from(it1);//这里要一个Iterable,所以你可以给他一个List,也可以给他一个Iterable
  // var s1 = Set.from([1,2,3,4,5]);
  print(s1);
  var s2 =Set.from(l1);
  print(s2);

  //通过上节课学到的is运算符 判断List是Iterable的子类
  Map m1 = {"name": "张三", "age": 18};
  var itm1 =  m1.entries.map((e) {
    print("m1遍历");
    return e ;
  });
  print(itm1);//Map.entries.map的打印也算遍历
  m1.forEach((key, value) {print("$key:$value");});  //Map自己的forEach
  l1.forEach((element) {print(element);});//Iterable的forEach
  if (l2 is Iterable) {
    print("l2属于Iterable");
  } else {
    print("l2不属于Iterable");
  }

  if (m1 is Iterable) {
    print("m1不是Iterable子类型");
  } else {
    print("m1不属于Iterable");
  }


   print(l1.first);
   print(l1.last);
   print(it1.first);
  print(it1.last);
/*
/// As long as the returned [Iterable] is not iterated over,
/// the supplied function [test] will not be invoked.
///只要返回的[Iterable]没有被遍历，
///提供的函数[test]将不会被调用。
 */
  l1.map((e){
    print("l1.map 遍历 $e");
  }).toList();
  it1.map((e){
    print("it1.map 遍历 $e");
  }).toList();
}
