// void main(){
// int main(){
main(List<String> list) {
  fun1();
  int age100_$ = 100; //变量必须由数字字母下划线美元符号组成

  int i1 = 100;
  i1 = 101;
  double f1 = 100.1;
  double f2 = 100;
  var v1 = 100;
  // v1 = 100.1;//这里报错,因为v1自动被上面推断为了int,所以不能再被赋值给double ,因为100.1这种带小数点的数字是double类型
  var v2 = 100.1;

  String str = "123";
  str = '456';
  str = '''
  abc
  456
  789
  ''';
  print("str=$str");

  //双引号可以里面嵌套单引号,单引号可以里面嵌套双引号
  String zhangsan = '张三外号叫"老六"';
  print("zhangsan=$zhangsan");
  String zhangsan2 = "李四外号叫'送分狂魔'";
  print("zhangsan2=$zhangsan2");
  //但是不可以双引号嵌套双引号,单引号嵌套单引号
  // String zhangsan3 = "李四外号叫"送分狂魔"";//报错
  // String zhangsan4 = '李四外号叫'送分狂魔'';//报错
  //
  const a = 100;
  // a = 200;//常量不能被复制
  // const b;//const在定义的时候就必须赋值

  final c = 100;
  // c = 101;//final不能被赋值
  final c2; //指说明了类型,但是没有给初始值,这种情况在其他语言叫做声明,赋初始值以后才叫定义.定义和声明的区别就是是否给了初始值
  c2 = 102; //可以,因为上面定义c2的时候没有初始化值.
  //final的作用
  final c3;
  c3 = DateTime.now(); //final可以获取时间,而且只能被赋值一次
  // c3 = DateTime.now();
  print("c3 = $c3");
/*
final 和const 都是定义常量
区别1:final是惰性初始化,使用时才进行第一次初始化,是懒加载
区别2:const必须用常量初始化,不能用方法函数可变的初始化
 */
}

void fun1() {
  print("123");
  print("adsff" + "123123");
}
