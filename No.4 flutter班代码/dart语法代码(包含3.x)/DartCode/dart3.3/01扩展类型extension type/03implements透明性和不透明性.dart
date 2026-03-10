// 透明性:当一个扩展类型用implements 实现了他的表示类型(封装的底层类型),可以视为:透明
// 不透明性:没有通过implements 实现他的表示类型

// extension type IntId(int value) {
extension type IntId(int value) implements int {
  //
  //如果不是透明的,不implements 实现 int,需要手动重写 +
  // int operator + (IntId other) => value + other.value;//不透明化要自己重写
  int get i1 => value;

  IntId get i2 => this;

  int get i3 => this;
}

main() {
  // int i1 = IntId(100);//把implements 继承int的 对象直接赋值给int ,因为v1implements int,具有透明性,可以当做int使用
  var i1 = IntId(100);
  int i9 =  IntId(100);
  // i9.i1;//错误,int不能调用getter
  print(i1.i1);
  print(i1.i2);
  print(i1.i3);

  var i2 = IntId(100);
  var i3 = IntId(100);
  // i1 + 10;
  // i1 + i3;
  // IntId i4 = 100;//类型不匹配
  List<IntId> list1 = [
    IntId(100),
    IntId(100),
    // 100////错误,元素类型` int `不能被赋值给列表类型` IntId2 `
  ];
  List<int> list2 = [
    100,
    200,
    IntId(100) //实现implements int以后透明化了,可以用 扩展类型的对象当做int使用
  ];
}
