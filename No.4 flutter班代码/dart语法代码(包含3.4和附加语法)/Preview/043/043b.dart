class Person043b {
  String name = "张三";
  int age = 22;
  double height = 170;
  int _id = 123;
  void _showInfo() {
    print("name = $name age = $age height = $height id = $_id");
  }
  //使用普通方法调用私有成员或者私有方法
  showPrivate(){
    print("_id = $_id");//调用私有成员
    _showInfo();//调用私有方法
  }
  set SetId(int id){
    _id = id;
  }
  get getId{
    return _id;
  }
}