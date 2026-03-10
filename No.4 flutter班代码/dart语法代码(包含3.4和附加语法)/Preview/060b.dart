//这个例子演示了 一个 常量构造函数,里面的参数是一个基本数据类型String和一个 类的对象,这个对象也是常量构造函数创建的
//
// flutter框架里面的Text 用常量构造函数 加const里面的 参数 样式style也是一个常量构造函数

//自定义的字体样式TextStyle1
class TextStyle1 {
  final int fontSize; //字体大小
  const TextStyle1(this.fontSize);
}

//自定义的文本框
class Text1 {
  final String data;
  final TextStyle1? style;
  static int a = 100;
  const Text1(this.data, {this.style});
}

main() {
  const Text1("abc",
      style:
          const TextStyle1(44)); //Text1的2个参数都是不可变的,第一个是常量字符串,第二个是一个 常量构造函数创建的对象
  String data = "abc";
  Text1(data, style: TextStyle1(44)); //可以传入一个变量
  // const Text1(data,
  //     style: TextStyle1(
  //         44));
  //报错,如果常量构造函数要求,里面参数也都是const,所以外层的Text1左边加了const,那么里面参数就必须是const,而data不是const

  Text1(data,
      style: const TextStyle1(
          44)); //外面的Text1没加const,所以,里面参数1,可以传入变量data,参数2 style 可以是const ,因为他传入的值是 常量44
  int fontSize = 44;
  // Text1(data,
  //     style: const TextStyle1(fontSize)); //错误 TextStyle构造函数加了const也要求里面的参数是不可变的
}
