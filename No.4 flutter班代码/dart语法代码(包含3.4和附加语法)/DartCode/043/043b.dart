class Person043b {
  String name = "张三";
  int age = 22;
  double height = 170;
  int _id = 100;

  void _showInfo() {
    print("name = $name age = $age height = $height id = $_id");
  }
  showPrivate(){
    _showInfo();
  }
  set SetId(int id){
    _id = id;
  }
  get getId{
    return _id;
  }
}