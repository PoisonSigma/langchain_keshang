main() {
  // 列表
  // [子模式1, 子模式2]
  // 列表模式外层匹配实现 List 的值，然后递归地将其子模式与列表的元素匹配以按位置解构它们：

  const a = 'a';
  const b = 'b';
  const c = 'c';
  var list = [a, b];
  switch (list) {
    // 列表模式 [a, b] 首先匹配 list，如果 list 是一个包含两个字段的列表，
    // 然后如果其字段与常量子模式 'a' 和 'b' 匹配。
    case [a, b]: //先看做一个整体的List进行匹配,然后进入子模式解构,a和b2个标识符,进行解构
      print('先匹配整体List模式,在匹配常量子模式 $a, $b');
    case [a, b, c]: //列表模式必须元素个数对上
      print('$a, $b $c');
    case [var a ,var b]:
      print('先匹配整体List模式再匹配 变量子模式 $a, $b');

  }
}
