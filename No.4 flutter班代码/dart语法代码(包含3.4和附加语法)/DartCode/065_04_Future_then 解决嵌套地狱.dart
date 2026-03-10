import 'dart:io';
//使用then解决嵌套地狱
//使用then解决嵌套地域,嵌套地狱,每一层执行完以后得结果,放在下一层中使用.{}大括号越扩层数越多
// 把第一层执行结果用return返回,下一层用then接受
main(){
  print("start");
  /*
    Future((){
      sleep(Duration(seconds: 1));
      var result = "abc";
      print("result = $result");
       Future((){
        sleep(Duration(seconds: 1));
        var result2 = "123";
        result += result2;
        print("result = $result");
        Future((){
          sleep(Duration(seconds: 1));
          var result3 = "xxx";
          result += result3;
          print("result = $result");
        }) ;
      }) ;
    });

   */



  Future((){
    sleep(Duration(seconds: 1));
    var result = "abc";
    print("result = $result");
    return result;
  }).then((value){
    sleep(Duration(seconds: 1));
    String result = value + "123";
    print("result = $result");
    return result;
  }).then((value){
    sleep(Duration(seconds: 1));
    String result = value + "xxx";
    print("result = $result");
  });
  print("end");
}