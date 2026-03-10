/*
枚举类型
枚举类型，通常称为枚举或enums，是一种特殊的类，用于表示一组固定数量的常量值。

注意：所有的enums都自动扩展Enum类。它们也是封闭的，意味着它们不能被子类化、实现、混合或以其他方式显式实例化。

抽象类和mixin可以显式实现或扩展Enum，但除非它们被enum声明实现或混入，否则没有对象可以实际实现该类或mixin的类型。

声明简单enums
要声明简单的枚举类型，请使用enum关键字并列出要枚举的值：
 */

enum Color{
  red,
  yellow,
  blue
}
main(){
   var color = Color.red;

   // var l1 = Color.values;// 要获取所有枚举值的列表，请使用enum的values常量。
   // for (var item in l1){
   //   print("item = $item");
   // }
   // print(Color.red.index);
   // print(Color.yellow.index);
   // print(Color.blue.index);

   int a = 30;
   switch(a ){
     case 10:
       print("10");
     case 20:
       print("20");
     case 30:
     case 40:
     case 50:
       print("30 40 50");
     default:
       print("默认操作,未找到匹配的值");
   }
    
   switch(color){
     case Color.red://注意switch在穷举enum的时候,需要把所有的值都穷举,否则switch报错
       print("红色");
     case Color.yellow:
       print("黄色");
     case Color.blue:
       print("蓝色");
     // default:
     //   print("默认颜色");
   }
   // var value = switch( 10  ){ 10=>10, 20=>20,_=>99  };
   // print(value);
}