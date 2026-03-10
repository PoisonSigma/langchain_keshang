//await是等待的意思, 作用是等待右边的异步 Future执行结束返回结果
//只要方法中使用了 await,就必须给函数添加async关键字,代表你的方法是异步方法,如果外界想要调用这个方法按照同步执行,调用这个方法时候也要加await
main() async {
  //注意下面代码没有在左边的值增加  await的时候,打印结果是i1=Instance of 'Future<int>' ,因为没有等待Future返回就向下执行了
  //Future 本身是一个抽象类,里面有泛型参数


  //Future.value工厂方法,返回一个Future对象,这个对象将来会完成,需要用await等待将来完成的值,这个值是value()括号里面的值
  var i1 = Future<int>.value(100);  //如果不加await那么i1等于 .valuefactory方法返回的Future对象
  /*
  var i1 = Future<int>.value(100);  //如果不加await那么i1等于 .valuefactory方法返回的Future对象
  // var i2 = Future<String>.value(100);//报错,String的泛型,不能给int的值
  var i3 = Future.value();//可以通过后面的赋值,直接让泛型确定真实的类型
  print(i1);
// await的作用,会等待右边Future对象执行完,返回给左边的
  //增加await以后,会等待右边直行完,返回给左边的i1 ,打印i1 = 100,把异步改成同步,代码会顺序向下执行
  var i2 = await Future.value(100);
  print("i2=$i2");


  //延迟返回Future.delayed 参数1,延迟时间,Duration()是dart中专门用来设置延迟时间的
  // seconds秒数
  //参数2,可以是一个匿名函数 FutureOr<dynamic> Function()?

    var f1 = await Future.delayed(Duration(seconds:1 ));
    //参数2是可选类型的Function类型,那么就可以传入参数,这样是直接干等2秒,因为参数2没传参,那么await等待返回的结果是null
  print("f1= $f1");

  //milliseconds 1000毫秒是1秒
  var f2 = await Future.delayed(Duration(milliseconds: 800),(){
    return "abc";
  });
  print("f2= $f2");
  //microseconds 微秒 1000000 100万 6个0是1秒

  var f3 = await Future.delayed(Duration(microseconds: 1000000),(){
    return "123";
  });
  print("f3= $f3");

print("end");
*/
  fun2();
var result3 =await fun3(); //因为fun3返回Future类型,那么也要用await等待才能得到 Future对象完成以后得值
print("result3 = $result3");
}


//函数如果 使用了await ,函数必须加上aysnc 把异步当做同步执行,同步就是要等待Future方法一行代码结束以后才向下执行
fun1() async {
  var result =  await Future.delayed(Duration(seconds: 1),(){
    return "abc";
  });
  print("fun1 result=$result");
  print("fun1 end");
}
fun2()   {
  // fun1();//因为fun1是异步方法,所以执行到这里的时候 直接向下执行打印 fun2 end
  //只要方法中使用了 await,就必须给函数添加async关键字,代表你的方法是异步方法,如果外界想要调用这个方法按照同步执行,调用这个方法时候也要加await
  // await fun1(); //如果用await等待fun1()执行完毕,才能变成同步,就是能顺序向下执行,但是fun2也会自动加上async
  print("fun2 end");
}

//Future作为函数返回值
Future<int> fun3(){
  return Future.value(100);
}