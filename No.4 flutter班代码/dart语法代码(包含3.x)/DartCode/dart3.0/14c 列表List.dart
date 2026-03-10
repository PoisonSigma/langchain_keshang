main(){
  // 列表
  // [子模式1, 子模式2]
  // 列表模式外层匹配实现 List 的值，然后递归地将其子模式与列表的元素匹配以按位置解构它们：
  const a = "a1";
  const b = "b2";
  const c = "c";
  var list = [a,b];
  switch(list){
    // case [a,b]: // 外层先匹配List列表模式,然后递归匹配里面的常量模式,进行解构
  // print('先匹配整体List模式,在匹配常量子模式 $a, $b');
    case [a,b,c]://列表模式位数要对应上
      print("$a $b $c");
    case [var a,var b]:
      print('先匹配整体List模式再匹配 变量子模式 $a, $b');
  }
}