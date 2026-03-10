/*
@redeclare
重新声明
#
声明一个扩展类型成员与超类型成员同名不像在类之间的覆盖关系那样，而是一个重新声明。扩展类型成员声明完全替换了任何同名的超类型成员。无法为相同函数提供替代实现。

您可以使用 @redeclare 注解告诉编译器您明知故选择使用与超类型成员相同的名称。如果这实际上不是真的，例如如果其中一个名称拼写错误，则分析器将提醒您。



extension type MyString(String _) implements String {
  // 替换 'String.operator[]'
  @redeclare
  int operator [](int index) => codeUnitAt(index);
}
content_copy
您还可以启用 lint annotate_redeclares，以便在声明隐藏超接口成员的扩展类型方法且未注释为 @redeclare 时得到警告。

用法
#

 */
extension type MyString(String str) implements String {
  // Replaces 'String.operator[]'

  // @redeclare
  int operator [](int index) => codeUnitAt(index);
}
main(){
  var s1 = MyString("abc");

  print( s1[0] );
}