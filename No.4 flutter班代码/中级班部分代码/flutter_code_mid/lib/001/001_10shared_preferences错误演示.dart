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
main(){
  // runApp(Text('asdfasddasfadsfadsfadsfadsfdsaffdsadfasdfas',textDirection:TextDirection.ltr ,));
runApp(MaterialApp(home: Scaffold(
  appBar: AppBar(title: Text("标题栏"),),
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
    late SharedPreferences pre;//会在初始化的一瞬间,爆红
   @override
   initState()  async {
    // TODO: implement initState
     //initState 不能返回Futrue类型,不能是异步的,解决方法,放在另一个函数里面
    super.initState();
        await Future.value("abc");//错误演示,不能是异步的initState
  }

  loadData() async {
    pre = await SharedPreferences.getInstance();
  }
  @override
  Widget build(BuildContext context) {
    loadData();
    read();
    return Column(
      children: <Widget>[
            TextField(
              controller: tc1,
              onChanged: (str){
                    print(str);
                  },
              decoration: InputDecoration(hintText: "请输入用户名"),
            ),
        TextField(
                  controller: tc2,
                  onChanged: (str){
                },decoration: InputDecoration(hintText: "请输入用户id")
                ),

        ElevatedButton(onPressed: () async {
                // tc1.text;
               pre.setString(Name, tc1.text);
               pre.setInt(ID, int.parse(tc2.text));
              }, child: Text("写入磁盘")),
        ElevatedButton(onPressed: (){

                      }, child: Text('读取磁盘'),
                )
      ],
    );

  }
  read(){


      name = pre.getString(Name) ?? "未找到姓名";
      id = pre.getInt(ID) ?? 0;
      print(name);
      print(id);

  }
}