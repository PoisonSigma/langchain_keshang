//this,指当前对象自己,对象方法访问自己对象里的方法和属性,可以省略

class Person {
  String name = "张三";
  int age = 0;
  double height = 180.5;

  //类的构造函数,对象创建时,自动执行的函数
  // Person(){
  //   print("构造函数Person()执行");
  // }
  // Person(String name , int age ,double height){
  //   this.name = name;
  //   this.age = age;
  //   this.height = height;
  //   print("构造函数Person()执行");
  // }
  Person(this.name ,this.age ,this.height){
      print("构造函数Person()执行");
  }

  //对象自己的方法可以访问自己的属性
  showInfo() {

    print("name = ${this.name} age = ${this.age}  height = $height");
  }
  growUp(){
    age++;
    print("当前年龄是 : $age");
    if(age < 25){
      //+= 自增操作  -=自减
      // height = height + 10;
      height += 10;
      print("身高是 $height");
    }else{
      print("岁数太大了, 不长了,身高是$height");
    }
}
}

main() {
  // var p1 = Person();
  var p1 = Person("李四",22,195.9);
  // p1.showInfo();

  p1.growUp();
  p1.growUp();
  p1.growUp();
  p1.growUp();
}
