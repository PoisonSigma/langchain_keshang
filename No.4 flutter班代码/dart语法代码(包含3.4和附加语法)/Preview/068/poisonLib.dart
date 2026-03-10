//这个例子中poisonLib.dart是库文件 p1.dart p2.dart p3.dart 是这个库的3个模块
//一个库里面可以有多个模块,一个模块里面可以有多个类,函数


//库文件中使用 library创建库
library poisonLib;
export 'dart:io'; //export是导出库,可以让引用当前库的文件,使用导出的库,例如当前所有import poisonLib 的文件,都可以不用包含dart:io库就能使用里面的方法
// 要放在 part 和 library之间 ,export导出文件以后,再使用这个库的文件,就不用再import dart:io库了


//模块一般用一个单独的文件保存,要引入库,就用part '文件名' 引入,如下引入'p1.dart  和 p2.dart'模块
part 'p1.dart';
part 'p2.dart';
// export 'dart:io'; //报错,放在了part 之后
//这里没有引入p3.dart,所以不能使用class P3