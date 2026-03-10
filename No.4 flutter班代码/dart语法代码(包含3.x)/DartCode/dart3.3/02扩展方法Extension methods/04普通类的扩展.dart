//普通的类也可以扩展
class A{
  
}
extension A2 on A{
  show(){
    print("show");
  }
}
main(){
    var a1 = A();
    a1.show();
}