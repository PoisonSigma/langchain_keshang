


//sealed 类不能在文件外被继承,sealed 的类不能在声明它的库之外直接 expends、implements 或mixin,
 sealed class Amigo {}

class Lucky extends Amigo {}
class Dusty extends Amigo {}
class Ned extends Amigo {}



//下面这些代码在076b.dart中会报错,因为在dart中每个文件就是一个库,在文件外sealed类型的class不能被  extends, implements,  mixin
class Bad extends Amigo {}

// 但这两个都是可以的：
class OtherLucky extends Lucky {}//没有传递限制,可以被当前文件无限继承
class OtherDusty implements Dusty {}

main(){

}