import 'StringA.dart';
import 'StringB.dart' hide StringB;//两个扩展里面有相同的 方法名,用hide 隐藏一个 扩展名
main(){
    "123".parseInt();
}