//普通的类也可以扩展
class A {}

extension A2 on A {
  show() {
    print("show");
  }
}

extension intExtension on int {
  show() {
    print("show");
  }
}

main() {
  var a1 = A();
  a1.show();

  int a = 100;
  a.show();
  100.show();
}
