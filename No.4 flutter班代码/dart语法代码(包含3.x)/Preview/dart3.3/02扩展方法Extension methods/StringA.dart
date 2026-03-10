/*
格式
extension 扩展名称 on 类型 {

}

 */
extension StringA on String {
  static String name = "自定义扩展StringA";//可以静态字段,有setter 和 getter
  // int length2 = 0;// 不能定义成员变量
  int get id => length;
  set id(int i){
      print("调用setter i =$i");
      name = "static静态成员name 被打印 id = $i";  //可以用setter保存当静态成员中
  }
  int parseInt() { //扩展方法
    try {
      return int.parse(this);
    }catch(e){
      print("发现异常e=$e");
      return -1;
    }
  }
// ···
}