//扩展类型中的静态方法和静态成员,可以存储数值
extension type IntId(int i){
        // int value1 = 0;//报错,不能创建成员变量
    static String id = "";
    int get value => i;
    set value(int i2){
      print("调用setter ,传入的值是 $i");
      // i = i2;//报错不能传给封装的底层表示类型
      id = "$i2";
    }
    //静态方法可以调用静态成员
    static changeValue(int i){
      print("调用静态方法");
      id = "${11000000000000 + i}";
    }
}
main(){
  /*
  var id1 = IntId(100);
    print(id1.value);
    id1.value = 200;
  // print(id1.value);
  print("调用 static ${IntId.id}");
  IntId.id = "300";
  print("调用 static ${IntId.id}");

   */
  // IntId.changeValue(20000102);
  // print(IntId.id);
  var id2 = IntId(100);
  dynamic id3 = IntId(100);
  // 动态类型不起作用的原因是扩展方法针对接收器的静态类型进行解析。
  // 由于扩展方法是静态解析的，因此它们的速度与调用静态函数一样快。

  id3.id = 200;//报错
}