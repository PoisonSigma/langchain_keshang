//泛型可以限制类的参数类型,下面是通过给类的构造函数传入参数,让泛型识别出指定的类型
import '053/053b.dart';

class Person<T> {
  T id;

  Person(this.id);

  showId() {
    print("T=$T");
    print("id=$id");
  }
}

main() {
  // var p1 = Person<int>(100);
  // p1.showId();
  //通过传入的参数,自动识别出泛型类型
  // var p2 = Person(3.14);
  // p2.showId();
  // var l1 = [1,2,3,4,5];
  // List l2;
  var l1 = ListPoison();
  l1.add(123);
  l1.add("abc");
  var values =  l1.values;
  print(values);
}
