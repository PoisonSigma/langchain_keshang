import 'dart:io';
import 'dart:math';

main() async {
  /*
    var f1 = File("a.txt");
  //以字符串形式写入
  f1.writeAsString("abc各位吴彦祖,高富帅");

   */
  /*
  var f2 = File("b.txt");
  //以字节方式写入
  f2.writeAsBytes([97,98,99]);
   */
  /*
  try {
    var f3 = File("c.txt");
    //创建一个写入文件的流,默认是打开以后从头写入,覆盖
    // IOSink sink = f3.openWrite(); //FileMode mode = FileMode.write默认参数是覆盖,从头写入
    IOSink sink = f3.openWrite(mode: FileMode.append); //FileMode mode = FileMode.write默认参数是覆盖,从头写入

    //add是在文件中写入
    sink.add([97, 98, 99]);
    sink.add([97, 98, 99]);
    await sink.close(); //关闭流,Future类型,要await
    print("end");
  }catch(e){
    print("e = $e");
  }
   */

  var s1 = Stream.fromIterable([97, 98, 99, 100]);
  var f4 = File("d.txt");
  var sink = f4.openWrite();
  /*
  //错误的方法是await,正确的是onDone
   */
/*
   await s1.listen((v){
    sink.add([v]);
  });
   sink.close();
   */
  s1.listen((v) {
    sink.add([v]);
  }, onDone: () {
    sink.close();
  });




  var l1 = <int>[];
  s1.listen((v) {
    print("v = $v");
    l1.add(v);
      // f4.writeAsBytes([v],mode: FileMode.append);
    // f4.writeAsBytes([97,98,99]);
    }, onDone: () {
    //拼接好以后可以写入文件,但是如果流过大,缓存有可能溢出.
      print("l1= $l1");
      f4.writeAsBytes(l1);
      sink.close();
    });

}
