import 'dart:io';

main() async {
  try {
    File file1 = File("a.txt");
    if (await file1.exists()) {
      print("文件存在");
    } else {
      print("文件不存在");
    }

    var content = await file1.readAsString();
    print(content);
    //返回readAsBytes  以字节形式读取 Bytes是字节,
    // Future<Uint8List>类型字节List,Uint8List 是无符号整数,长度是8位二进制,存储0~255的无符号整数
    var content2 = await file1.readAsBytes();
    print(content2);
    for (var item in content2) {
      print("item=$item");
    }
  }on FileSystemException{
    //打不开文件有指定的类型异常
    print('文件类型异常');
  }
  catch(e){
    print("e = $e");
  }
}
