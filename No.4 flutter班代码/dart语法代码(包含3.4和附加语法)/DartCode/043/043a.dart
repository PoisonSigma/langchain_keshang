// dart中定义私有成员或属性不是用的private 或者 protected 受保护的关键字,而是用下_划线开头
// 在同一个文件下,_开头的对象的私有方法和私有成员可以被访问
// 不在同一个文件下,import引入进来的不能访问_开头的私有成员
// 使用普通方法访问私有方法和私有成员变量



import '043b.dart';

main(){
    var p1 = Person043b();
    p1.age;
    p1.name;
    p1.SetId = 99999;
    p1.showPrivate();
    print("_id=${p1.getId}");
    // p1._id;
    // p1._showInfo();

}