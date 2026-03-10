class Person {
  //属性只要不是可选的,就都要初始化
  String? name;
  int age; // age和final a可以加上late,这样赋值和初始化结果就一样了
  final int a;

  //下面是是构造函数简写
  // Person(this.name,this.age,this.a);
  //下面这样就不行,age和 a都没有初始化,而是赋值 ,
  // Person(String name,int age ,int a){
  //   this.name = name;
  //   this.age = age;
  //   this.a = a;
  // }
  showInfo() {
    print("name = $name age =$age a = $a");
  }

//初始化列表的作用,跟上面的构造函数简写,作用相同,都是在创建对象的时候给属性初始化,
// 而不是在{}大括号里面赋值,大括号里面赋值,是对象已经创建完以后再执行的操作
  //语句之间用逗号,分割
//   Person(String name,int age ,int a):this.name = name , this.age = age ,this.a = a;
  //等价于下面
// Person(this.name,this.age,this.a);

//不能在初始化列表里面执行赋值之外的其他操作,例如打印
//   Person(String name,int age ,int a):this.name = name , this.age = age ,this.a = a,print("123");//报错
//下面代码作用是,如果final a 传入的值是null,那么就让a 有一个默认值100

// Person(this.name,this.age,[int ?a]):this.a = a ?? 100;

  //  上面写法 等价于下面,
  // Person(this.name, this.age, [this.a = 100]) {}
//不能用构造函数简写和初始化列表给属性初始化2次
// Person(this.name,this.age,this.a):this.name = 100;// was already initialized by this constructor


  //初始化列表里面可以使用 3元运算符 ?

  //简写方式只能给默认值赋值常量,不能用 ? 三目运算符
  // Person(this.name,this.age,{ this.a = 100}){
  // }
// Person(this.name,this.age,{ this.a =  age == 18 ? -1 : 0}){  //报错The default value of an optional parameter must be constant. 可选参数的默认值必须为常数。
// }
  //在初始化列表里面, a的值等于 三元运算符,如果 age 等于18 ,a = -1 否则 为0
 // Person(this.name,this.age): a = age == 18 ? -1 : 0{
 //
 //  }

  //??= 的意思是,如果 左边的值为 null,则 赋值右边的值
  Person(this.name,this.age, this.a){
      name ??= "未知姓名"; //如果name为null,那么就赋值成  "未知姓名"
  }
}

main() {
  // var p1 = Person("张三", 18, 1000);
  // var p1 = Person("张三", 18);
  // p1.showInfo();
  // var  p1 = Person("张三",18,a:15);
  var  p1 = Person(null,19,100);
  p1.showInfo();
}
