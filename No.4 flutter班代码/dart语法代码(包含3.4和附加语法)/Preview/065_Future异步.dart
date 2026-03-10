
import 'dart:io';

main() {
  /*
  print("start");
  // sleep(Duration(seconds: 2));
  getData();
  print("end");

   */


  // Function a = getData;
}

getData() {
  Future(() {
    print("Future start");
    sleep(Duration(seconds: 2));
    print("Future end");
    return "网络数据";
  }).then((value) => print(value));
}
/*
 factory Future(FutureOr<T> computation()) {
    _Future<T> result = new _Future<T>();
    Timer.run(() {
      try {
        result._complete(computation());
      } catch (e, s) {
        _completeWithErrorCallback(result, e, s);
      }
    });
    return result;
  }
 */
