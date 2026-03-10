class ShoppingCartItem{
  String text;
  String img;
  bool selected;
  int count;

ShoppingCartItem({required this.text,required this.img,required this.selected,required this.count});
}
main(){
  var item1 = ShoppingCartItem(text: "哈尔滨吴彦祖", img: "images/7dsf", selected: true, count: 10);
  // print(item1.imgs);//模型的好处是,拼写错误,编译器会报错
  var map1 = {"text":"哈尔滨吴彦祖",
  "img":  "images/7dsf",
    "selected":true
  };
  //下面是map的形式,
  print(map1["text"]);
  print(map1["imgs"]);//这个就是拼写错误以后,得不到数据的演示,多加了一个s
  print(map1["selected"]);
}