// 透明性:当一个扩展类型用implements 实现了他的表示类型(封装的底层类型),可以视为:透明
// 不透明性:没有通过implements 实现他的表示类型

extension type IntId(int value) implements int {
  int get i1 => value;//返回底层类型
  IntId get i2 =>this;//这里因为implements int,所以this,就是当前对象可以当做int类型使用,所以返回this
  int get i3 => this;  //这样也行,this也是int

}

//IntId2没有implements实现他的表示类型,就是不透明的
extension type IntId2(int value){

}
//一旦 implements某个类型以后,用对象返回底层类型
void main () {

  var v1 = IntId(100); // v1 类型: NumberT
  int i1 = v1;//把implements 继承int的 对象直接赋值给int ,因为v1implements int,具有透明性,可以当做int使用
  int i1b = IntId(200);


  // int i2 = IntId2(100);//错误 IntId2没有implements实现它的表示类型,不是透明的,不能当做表示类型int使用
  List<IntId>list1 = [
    IntId(100),
    IntId(200),
    // 300,//错误,元素类型` int `不能被赋值给列表类型` IntId2 `
  ];
  List<IntId2> list2 = [
    IntId2(100),
    IntId2(200),
    // 300,//错误,元素类型` int `不能被赋值给列表类型` IntId2 `
  ];
  List<int> list3 = [
    100,
    200,
    IntId(300),//正确
    // IntId2(400),//错误IntId2没有implements int不是透明的,类型不匹配
  ];

  /*
  // 错误：扩展类型接口对表示类型不可用
  i1.i1;
   */
  int v2 = IntId(2); // v2  右边是 扩展类型 的对象,左边直接是 int类型
  var i3 = IntId(10) - IntId(8);
  print(i3);

}