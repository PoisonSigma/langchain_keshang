/*
枚举类型，通常称为枚举或enums，是一种特殊的类，用于表示一组固定数量的常量值。
 */
enum Color{
  red,
  yellow,
  blue
}
/*
class Color2 extends Colors{
}
//不能被子类化
 */


main(){
  var color = Color.red;
  showColor(color);
  // 要获取所有枚举值的列表，请使用enum的values常量。
}
void showColor(Color color){
  switch(color){//注意switch在穷举enum的时候,需要把所有的值都穷举,否则switch报错
    case Color.red:
      print("红色");
    case Color.yellow:
      print("黄色");
    case Color.blue:
      print("蓝色");
    default:
      print("没找到颜色");
  }
}