import '053/053b.dart';
//泛型可以限制类的参数类型,下面是通过给类的构造函数传入参数,让泛型识别出指定的类型
class Person<T>{
  T id;
  Person(this.id);//构造函数中传入的参数id,因为id被定义为T类型,所以在这时,T被识别出传入的类型.
  showId(){

    print("T=$T");//打印类型
    print("id=$id");
  }
}

main(){
  //通过传入的参数,自动识别出泛型类型
  //  var p1 = Person("abc");
  //  p1.showId();
  //  var p2 = Person(123);
  //  p2.showId();
  //
  //  var l1 = [1,2,3,4,5];
  //  l1.add(888);
  //  print(l1);
  //
  //  var lp1 = ListPoison();
  //  lp1.add(3);
  //  lp1.add(5);
  //  // print(lp1._l1);//错误,文件外import包含进来的不能访问私有属性
  //  print(lp1.values);



}