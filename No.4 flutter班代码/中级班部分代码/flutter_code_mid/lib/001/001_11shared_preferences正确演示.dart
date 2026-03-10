//为了演示完整的获取并且保存token,需要使用本地存储插件shared_preferences
//pub.dev查找
// shared_preferences
//pubspec.yaml中添加shared_preferences: ^2.2.3
//为了演示完整的获取并且保存token,需要使用本地存储插件shared_preferences
//pub.dev查找
// shared_preferences
//pubspec.yaml中添加shared_preferences: ^2.2.3
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

String Name = "name";
String ID = "id";

main() {
  // runApp(Text('asdfasddasfadsfadsfadsfadsfdsaffdsadfasdfas',textDirection:TextDirection.ltr ,));
  runApp(MaterialApp(
      home: Scaffold(
    appBar: AppBar(
      title: Text("标题栏"),
    ),
    body: HomePage(),
  )));
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String name = "";
  int id = 0;
  var tc1 = TextEditingController();
  var tc2 = TextEditingController();
  var _pre = SharedPreferences.getInstance(); //会在初始化的一瞬间,爆红
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    read();
  }
  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        TextField(
          controller: tc1,
          onChanged: (str) {
            print(str);
          },
          decoration: InputDecoration(hintText: "请输入用户名"),
        ),
        TextField(
            controller: tc2,
            onChanged: (str) {},
            decoration: InputDecoration(hintText: "请输入用户id")),
        ElevatedButton(
            onPressed: () async {
              // tc1.text;
              var pre = await _pre;
              pre.setString(Name, tc1.text);
              pre.setInt(ID, int.parse(tc2.text));
            },
            child: Text("写入磁盘")),
        ElevatedButton(
          onPressed: () async {
            read();
          },
          child: Text('读取磁盘'),
        ),
        Text('姓名:$name'),
        Text('id:$id'),
      ],
    );
  }

  read() async {
    print("read");
    var pre = await _pre;
    setState(() {
    name = pre.getString(Name) ?? "未找到姓名";
    id = pre.getInt(ID) ?? 0;
    print(name);
    print(id);
    });
  }
}
