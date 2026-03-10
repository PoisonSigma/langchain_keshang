//dart 3.0的元组 Records类型(元素1,元素2,元素3...) (swift中的元组),小括号里面可以是任意类型
main() {
//注意,Record类型的创建不用使用Record关键字,而是要使用类型注释(int,int)或者使用var
  Record r = (123, 455);
  print("r类型=${r.runtimeType}");

  //类型注释(类型,类型),例如(int, int)
  //Record类型注释是由括在括号中的类型的逗号分隔列表组成。您可以使用record类型注释来定义返回类型和参数类型。
  (int, int) r0 = (123, 456);
  var r1 = (123, 456);
  print("r1类型=${r1.runtimeType}");
  int a;
  int b;
  // 解构Destructuring
  //解构:像swift中的元组那样使用, 把()小括号里面对应的位置,放上变量进行接收
  //解构在后续的模式课程中会详细讲解:解构是用一组变量,去分解相同形状的一组值.
  (a, b) = r1;
  print("a= $a");
  print("b= $b");
  (a, b) = (100, 99);
  print("a= $a");
  print("b= $b");

  //简单练习一下解构 用在List中
  var l1 = [1, 2, 3, 4];
  int c, d;
  [a, b, c, d] = l1;
  print("a = $a b= $b c = $c d = $d");
  //解构 用在Map中
  {"money": a, "age": b} = {"money": 99999, "age": 18};
  print("a = $a b= $b");



  //$1,$2分别对应元祖的第一个和第二个位置的值,这里的1和2是位置字段

  a = r1.$1; //$1代表位置字段1的值
  b = r1.$2; //$2代表位置字段2的值
  print("a= $a");
  print("b= $b");
  //r1 = ("abc",123,456);//报错,类型不匹配 不能从 '(int, int)' 转到 (String ,int ,int)
  var r2 = ("abc", 123, 456);
  Record r3 = ("abc", 123, 456);
  r3 = r2;

  var p1 = (a: 1);

  //这个例子是元组里面有3个int,分别用3个变量解构
  int x, y, z;
  (x, y, z) = (1, 2, 3);
  print("x =$x  y =$y  z= $z");

//Records表达式是由命名字段或位置字段的逗号分隔列表组成

//下面a1,a2是命名字段,$1$2是位置字段
  var r4 = (a1: 100, a2: 200, 300, 400);
  r4.a1;
  r4.a2;
  r4.$1;
  r4.$2;
  //命名字段,不能乱起名字
  // var r5 = (1: 100,a2:200,a3:300,a4:400);//1不能当做命名字段使用 ,报错Expected an identifier, but got '1'.

  print(r4.a1);

  var r5 = (100, a1: 150, 200);
  r5.$1;
  r5.a1;
  r5.$2;
  print("r5 = ${r5.$1} ${r5.a1} ${r5.$2}");

  //下面演示命名字段和位置字段混合的解构元组
  int z1, z2, z3, z4;
  (a1: z1, a2: z2,  z3,  z4) = r4; //注意左边匹配的id要跟右边的r4的命名字段和位置字段相同
  print("z1 = $z1 z2 = $z2 z3 = $z3 z4 = $z4");

//带命名字段的 类型注释 语法:用 {}大括号把命名字段括起来,例如下面{}里面的命名字段a和b
  ({int a, bool b}) r6;//先声明
  //再赋值
  r6 = (a: 123, b: true);

  ({int c , int d}) r7 = (c:100,d:200);  //直接用类型注释 定义带明明字段的元组再赋值

    //命名字段不一样不能赋值
    // r6 = r7;//编译错误,命名字段a,b 和 c,d不一样,不能赋值
  //命名字段不相同,不能赋值.


  //在record类型注释中，您还可以为位置字段命名，但是这些名称仅用于文档，不影响record的类型：
  (int a , int b) r8 = (1,2);//在小括号里的是位置字段,分别给他们字段名,起了a和b
  (int c ,int d)r9 = (100,200);
  r8 = r9;//编译正确,给位置字段$1$2命名,不会影响使用
  r8.$1;//位置字段没有改变,没有变成a
  r9.$1;


  // Record相等性
  // 如果两个records具有相同的形状（字段集合）并且它们对应的字段具有相同的值，则它们相等。
  //位置字段命名以后,不影响判断值

  // 例如：下面是小括号,说明不是命名字段,而是位置字段.

    (int x, int y, int z) point = (1, 2, 3);
  (int r, int g, int b) color = (1, 2, 3);

  print(point == color); // 打印 'true'。

  //{}大括号里面是命名字段,命名字段不同,用==双等号判断就不同
    ({int x, int y, int z}) point2 = (x: 1, y: 2, z: 3);
  ({int r, int g, int b}) color2 = (r: 1, g: 2, b: 3);

  print(point2 == color2); // 打印 'false'。提示：Equals on unrelated types。



  //record的多返回值,通过解构来完成

  (String,int) userInfo(){
        return ("张三",18);
  }
   var (name,age) = userInfo();//用一个元组接收返回的一个元组,通过2个变量解构
  print("name = $name");
  print("age = $age");


}
