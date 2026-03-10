//this,指当前对象自己,可以用来对象方法访问自己对象里的方法和属性,可以省略

//类的构造函数,对象创建时,自动执行的函数
class Person {
  String name = "张三";
  int age = 22;
  double height = 170;
  // Person(String name, int age,double height) {
  //   this.name = name;
  //   this.age = age;
  //   this.height = height;
  // }


  Person(this.name,this.age,this.height);

  // Person() {
  //   print("构造函数 Person()执行");
  // }

  growUp() {
    this.age++; //这里长大就是让对象方法让对象自己的属性age+1
    print("当前年龄= $age");
    if (this.age < 25) {
      //+= 是让变量自增
      //相当于 this.height = this.height+10;
      this.height += 10; //
      print("身高是  ${this.height}");
    } else {
      ////this可以省略
      print("岁数大了,不长了,身高是  $height");
    }
  }
}

class Person2 {
  String name; //当一个属性没有默认值的时候,在构造函数中,要给他传入初始化的值
  int age = 18;

  // Person2(String name, int age) {
    //Non-nullable instance field 'name' must be initialized. (Documentation)  Try adding an initializer expression, or add a field initializer in this constructor, or mark it 'late'

    Person2(this.name){
    // this.age = age;
  }
  // Person2(this.name) {
  //   //这句话等于是把this.name在构造函数传入的时候赋值
  // }

  // Person2(this.name, this.age) {
    //报错The unnamed constructor is already defined. 未命名的构造函数已经定义.
  //   print("构造函数Person2(this.name, this.age)执行");
  // }
  showInfo() {
    print("name = $name age = $age");
  }
}

main() {

  // var p1 = Person(); //自动执行默认的构造函数
  // var p1 = Person("张三", 18);//当默认的构造函数有了参数,Person()这种格式,小括号里面的也要传入参数
  // p1.growUp();
  // p1.growUp();
  // p1.growUp();
  //这里没法使用this,因为this是在类内定义的时候使用的,当前作用于是main方法内
  // p1.this.age;//不能这么写,在类外面对象变量p1,就是指p1对象了,不需要加this

  // var p2 = Person2("张三", 18);
  // p2.showInfo();
}
