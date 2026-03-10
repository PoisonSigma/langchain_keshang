/*
[]位置可选参数 ,[]中括号里面的参数顺序不能换,因为[]中括号中的参数是可以不传入的,所以必须是可选类型,或者给默认值
{}命名可选参数,{}大括号里面的参数名字必须传入,位置可以换,有required关键字作为必填项,不能有默认值,因为一定会传入
required的精髓就是,可以在调用的时候自动填写出参数名,但是如果不填写required不会自动填写参数名,因为参数也可能是程序员自己故意不填写的
 */
fun1(int a,[int ? b ,int ? c]){
  print("a= $a b=$b c=$c"); //不传入值的话,默认是null
}
fun2(int a,[int ? b = 999 ,int ? c = 999]){//不传入值的话,有默认值
  print("a= $a b=$b c=$c");
}
fun3(int a,[int  b = 999 ,int  c = 999]){//有默认值,可以是非可选类型
  print("a= $a b=$b c=$c");
}
// fun3(int a, [int b , int c ]) {  //报错,因为位置可选参数可以不传入值,不传入值,默认是空,空的话,必须用可选类型接收.
//   print("a= $a b=$b c=$c"); //不传入值的话,有默认值
// }

//命名可选参数调用的时候必须有参数名字
fun4(int a ,{int? b = 999,int? c =999}){
  print("a= $a b=$b c=$c");
}
fun5(int a ,{int b = 999,int c =999}){
  print("a= $a b=$b c=$c");
}
fun6(int a,{required int? b , required int c}){
  print("a= $a b=$b c=$c");
}
fun7(int a,{required int? b  , required int c}){
  print("a= $a b=$b c=$c");
}
main(){
  // fun1(100);
  // fun1(100,200);
  // fun2(100);
  // fun3(100);
// fun4(100);
// fun6(100, b: 100, c: 100);
fun6(100,  c: 200, b: null);
}