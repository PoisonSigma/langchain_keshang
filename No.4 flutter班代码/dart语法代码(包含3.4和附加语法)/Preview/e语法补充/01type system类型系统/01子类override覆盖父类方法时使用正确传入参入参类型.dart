

/*
//这个例子演示 子类重写父类方法,传入参数的规定
当覆盖方法时，请使用正确的传入参数类型:(父类或者超类)
覆盖方法的参数必须是与父类中相应参数的类型相同或是其超类型。不要通过将类型替换为原始参数的子类型来“收紧”参数类型。
注意：
如果您有使用子类型的有效理由，可以使用covariant关键字。
考虑Animal类的chase(Animal)方法：
 */

class Animal {
  void eat(Animal a) {}//这个父类的函数为了演示重写override覆盖函数的时候参数必须是父类或者超类
}

//✔ 静态分析：成功


class Dog extends Animal {
  //正确 重写函数的参数是 父类型 或者 超类
  // @override
  // void eat(Animal a) {} //正确 重写函数的参数是父类型方法的传入类型 或者 超类
  // void eat(Object a) {} //正确,参数是超类,父类方法中定义的传入参数的父类

  // void eat(Dog a) {}//错误,重写的函数传入参数不能是子类
//这里的代码不安全,因为,可能会调用Animal的子类Cat的对象,传入到这里的eat,就没法传入,但是如果传入父类函数要求的Animal类型,就可以把其他子类,例如Cat传入进来
//

}
class Cat extends Animal{
}
main() {
      Animal a1 = Dog();
      a1.eat(Cat());//这里演示如果void eat(Dog a) {} 这样定义了方法,那么这样调用传入了Animal的其他对象,例如Cat()对象,那么void eat(Dog a) {}接受不了
}