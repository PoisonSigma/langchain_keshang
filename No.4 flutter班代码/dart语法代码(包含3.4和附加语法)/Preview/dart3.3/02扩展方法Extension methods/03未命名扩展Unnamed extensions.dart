//未命名的扩展方法只能在当前包中进行使用,无法在包之外使用,也不能解决被包含以后得冲突问题
extension on String{
      int parseIntUnamed(){
        return int.parse(this);
      }
}
main(){
  int a = "123".parseIntUnamed();
  print(a);
}