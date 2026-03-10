import 'dart:io';

main() async {
  //sleep()睡眠一会,程序停止运行 sleep(Duration(seconds: 1));//睡眠1秒
  //使用sleep实现delayd功能
//普通的delayed,是否有await都会执行
  Future.delayed(Duration(seconds: 1),(){
    print("delayed执行");
  });

  //下面因为 value里面放的不是一个值,而是一个闭包,所以要调用闭包,我们用 await接受一下.
  //  var fn1 = await Future.value((){
  //
  //    sleep(Duration(seconds: 1));
  //    print("闭包1执行1");
  // });
  //  fn1();




  //then的效果是可以不用使用await等待Future完成时候返回的结果,就能异步向下执行,并且等待结果完成以后对返回的值进行操作
  //例如下面result 得到返回的Future对象,并且向下异步执行,进行打印result,1秒钟延迟之后.then接收到闭包里面执行的结果,并且对结果进行后续打印操作

  /*
  var result =  Future.delayed(Duration(seconds: 1), () {
      print("闭包1执行");
    return "abc";
  }).then((value) => print(value));

  print("result= $result");
*/

  //不用await接受也可以执行.value
  Future.value((){
    sleep(Duration(seconds: 1));
    print("value执行的内容执行");
  }).then((value) {
    //这里的value是上面整个.value()里面的闭包.是一个function变量,所以调用他用value();
    value();
    print("then执行");
  });


  //如果是带then的Future会把最后一个then返回的结果返回给await,例如下面会把最后一个"abc"返回给result2
  /*
  var result2 =await Future.delayed(Duration(seconds: 1),(){
        print("闭包2执行");
        sleep(Duration(seconds: 1));//睡眠1秒
        return 1000;
    }).then((value) {
        //then的返回值依然是一个Future对象,如果不返回Future就是null
        //then里面闭包的返回值,是Future对象完成的结果,可以用await 同步接受,也可以继续用then来异步操作接受
        print("then接收到结果 value = $value");
        sleep(Duration(seconds: 1));//睡眠1秒
        return "abc";
    });

   */
  // .then((value) => print("第二个then执行 value = $value"));
  // print("result2=$result2");

  //使用then解决嵌套地狱
  //  var r = await Future.delayed(Duration(seconds: 1),(){
  //    var result1 = 1+2;
  //    print("第1层执行 result1 = $result1");
  //
  //    Future.delayed(Duration(seconds: 1),(){
  //      var result2 = result1 + 10;
  //      print("第2层执行 result2 = $result2");
  //      Future.delayed(Duration(seconds: 1),(){
  //        var result3 = result2 + 10;
  //        print("第3层执行 result3 = $result3");
  //      });
  //    });
  // });

  //使用then解决嵌套地域,嵌套地狱,每一层执行完以后得结果,放在下一层中使用.{}大括号越扩层数越多
  // 把第一层执行结果用return返回,下一层用then接受
  // Future.de

  //抛出异常的时候,可以用onError接收到抛出的异常 ,error是捕获的异常,stackTrace (可以忽略)堆栈跟踪显示你都调用了哪些方法,
  // 当onError捕获异常的时候catchError就不会捕获异常
   /*
  Future.delayed(Duration(seconds: 1), () {

    print("第1层");
    throw(IOException);
    return "abc";
  })

      .then((value) => print("第2层value = $value"))
      .onError((error, stackTrace) =>
          print("onError error = $error ,stackTrace = $stackTrace "))
      .catchError((error, stackTrace) =>
          print("catchError error = $error ,stackTrace = $stackTrace "))
  .whenComplete(() {
  //whenComplete是抛出异常也会执行的代码,如果不抛出异常,那么就会按照顺序执行,whenComplete放在哪里就在哪里执行,放在中间和结尾都行
  print("whenComplete执行");
  });

    */
}
