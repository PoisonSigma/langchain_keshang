import '01extension type扩展类型.dart';

main(){
  // var id4 = IntId3._(100);//文件之外私有的命名构造函数不能调用
  var id4 = IntId3(100);//未命名的构造函数
}