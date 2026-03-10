//扩展类型中的静态方法和静态成员,可以存储数值
extension type IntId(int i){
  // int i2 = 0;//报错普通的成员变量不能定义
  static String id = "";//可以,静态成员可以使用,作用可以用来保存setter写入的值
  static changeValue(int i){
    id = "$i";//静态方法可以修改静态变量
    print("调用静态方法, value = $id");
  }
  set setValue(int i){
    id = "${11000000000000+i}"; //北京身份证开头
    print("setter方法 value = $id");
  }
}
main(){
/*
  var id1 = IntId(100);
  IntId.changeValue(200);
  print(IntId.id);//静态成员getter
  IntId.id = "20000103";//静态成员 setter
  print(IntId.id);//
  id1.setValue = 20000102;//00年1月2日出生的身份证
*/
  var id2 = IntId(300);
  id2.setValue = 400;
  print(IntId.id);//静态变量和 静态方法都是属于 扩展类型的,不是属于单独一个对象的

}



