// 强制转换
// 使用as强制类型转换
//
// 强制转换模式允许您在解构之前在中间插入类型转换，然后将该值传递给另一个子模式：
main() {
  /*
    num n1 = 100;
    n1 = 3.14;
    var n2 = n1 as int; //as 强制类型转换

    n2 = 100;
    // n2 = 3.14;

    int a = 1;
    double f = 3.14;
    print(n1.runtimeType);
   */
  /*
  (num, Object) r1 = (1, "abc");
  // r1 = (3.14,100);
  // var (a,b) = r1;
  // a =3.14;
  // b= 100;
  // b = "zhang3";
  var (a as int, b as String) = r1;
  a = 100;
  // a = 3.14;//报错,类型错误
  b = "abcde";
  // b = 100;//报错,类型错误
/*
  //转换失败,会抛出异常
  try {
    int i1 = 100;
    i1 as String;
  }catch(e){
    print("e = $e");
  }
 */
*/
  (num, Object) r1 = (1, "abc");


  try {
    var (a as String,b) = r1;
  }catch(e){
    print("e = $e");
  }
  // 'int' is not a subtype of type 'String' in type cast
  // 在类型转换中'int' 不是 'String' 类型的子类型

}
