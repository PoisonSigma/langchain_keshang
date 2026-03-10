main(){
  // 强制转换
  // 使用as强制类型转换
  //
  // 强制转换模式允许您在解构之前在中间插入类型转换，然后将该值传递给另一个子模式：
  //   int a = 1;
  //   double f = 1.0;
  (num, Object) record = (1, 's');  //num是所有数字类型的父类,例如int double,里面有一些数学运算 加减乘除 大于小于关系等
  record = (3.14,100); //因为null也可以是double,所以可以复制成3.14 ,Object可以是数字,所以可以复制为100
  print(record.runtimeType);
  // var (i as int, s as String) = record;
  // print(i.runtimeType);
  // print(s.runtimeType);
  // 如果值没有声明的类型，则强制转换模式将抛出异常。与空断言模式类似，这允许您强制断言某个解构值的预期类型。
  try {
    var (i as String, s as String) = record; //报错,类型转换错误,只有int无法转换成String
    print(i.runtimeType);
    print(s.runtimeType);

    // 'int' is not a subtype of type 'String' in type cast
    // 在类型转换中'int' 不是 'String' 类型的子类型
  }catch(e){
    print("e = $e");
  }


}