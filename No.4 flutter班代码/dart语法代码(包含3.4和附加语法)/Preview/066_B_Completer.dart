import 'dart:async';

Future<void> waitForSomethingAsync() async {
  // 创建一个Completer实例
  Completer completer = new Completer();

  // 模拟异步操作，比如等待用户输入或网络请求
  /*
  Timer.run(() {
    // 模拟异步操作完成
    // 可以在这里处理异步操作的结果，然后完成Future
    print("异步操作完成");
    completer.complete(); // 完成Future，不传递值
  });

   */
  (){
    print("开始");
    completer.complete("abc");//让completer的状态变成完成
  }();
  // 等待异步操作完成,如果上面没有completer.complete(); 那么下面就不执行
  var result = await completer.future;
  print("继续执行后续代码");
  print("result = $result");


}

void main() {
  waitForSomethingAsync();
}