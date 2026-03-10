//1.main() 不写返回类型那么就是dynamic类型,运行时候自动推断返回类型
// main(){
//
// }
//2.void main() 无返回类型
// void main(){
//   // return 1;//不可以返回值
// }
//3.int main() 返回整形
// int main(){
//    return 1;//不可以返回值
// }
//4.main( List list)带参数列表,可以给主函数传送参数
// main(List<String> list){
//  print("main函数被调用,传入的值是:$list");
// }
//main函数的参数列表只能是List<String>,不可以是其他的类型,否则报错
//4.1 main(List<int> list){
//}

//在终端调用dart run指令运行dart文件
//参数可以用逗号或者空格隔开,可以写冒号,也可以不写
//dart run 014.dart x,y,zxb
//dart run 014.dart "abc" "123" "122"
//dart run 014.dart "abc" "123","122"

//5,以上调用方法的返回类型可以随意组合

//5.1返回int
// int main(List<String> list){
//   print("main函数被调用,传入的值是:$list");
//   return 1;
// }
//5.2 void不返回任何值
// void main(List<String> list){
//   print("main函数被调用,传入的值是:$list");
// }

//5.3dynamic返回dynamic,默认什么都不写返回类型就是dynamic
dynamic main(List<String> list){
  print("main函数被调用,传入的值是:$list");
}