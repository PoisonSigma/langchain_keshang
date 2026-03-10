//这个例子演示了 一个 常量构造函数,里面的参数是一个基本数据类型String和一个 类的对象,这个对象也是常量构造函数创建的
//
// flutter框架里面的Text 用常量构造函数 加const里面的 参数 样式style也是一个常量构造函数
class TextStyle1 {
  final int? fontSize; //字体大小
  const TextStyle1({this.fontSize});
}

class Text1 {
  final String data;
  final TextStyle1? style;

  const Text1(this.data, {this.style});
}

main() {
  Text1("abc", style: const TextStyle1(fontSize: 100));

  int fontSize = 100;
  // Text1( "abc" ,style:  TextStyle1(fontSize: fontSize));
  Text1("abc", style: TextStyle1(fontSize: fontSize));

  String data = "abc";
  Text1(data, style: const TextStyle1(fontSize: 100));
}
