import 'dart:io';
import 'dart:math';

import 'package:dio/dio.dart';

import 'common.dart';

main() async {
  try {
  final dio = Dio(BaseOptions(baseUrl: baseUrl));
    var res = await dio.get("file",options: Options(responseType: ResponseType.stream));
      if (res.data.stream is Stream){ //为了编写代码翻遍,这里用is判断类型以后,给一个明确类型,不是动态类型
        Stream s1 =  res.data.stream;
        // 这是你要写入的文件路径
        // var file = File("08.txt");//txt结尾预览的时候就会按照文件格式预览
        var file = File("08.jpg");//按照图片格式预览
        //创建一个写入文件的流,默认是打开以后从头写入,覆盖
        IOSink sink = file.openWrite();
        s1.listen((v) {
          print("v = $v");
          sink.add(v);
        },onDone: (){ //注意,建议用onDone去处理订阅结束之后的操作,例如文件流关闭
          sink.close();
        }
        );

      }
      // sink.close();
    }catch(e){
      print("e = $e");
    }
}