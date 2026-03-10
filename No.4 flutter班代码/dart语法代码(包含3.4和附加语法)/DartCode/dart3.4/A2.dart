class A2 {
  String name = "";
  int age = 0;

  A2.fromMap(Map map){
    try {
      name = map['name'] ?? "";
      age = map['age'] ?? 0;
    }catch(e){
      print("错误e=$e");
    }
  }
  A2({
    required this.name,
    required this.age,
  });

  @override
  String toString() {
    return "name:$name,age:$age";
  }
}