
import 'package:flutter/material.dart';

main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text('标题栏'),
          ),
          body: const HomePage())));
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  var isSelected = true;
  var selectIndex = -1;//设置选中的序列,注意这个不用放在build里面,否则每次刷新页面,他都变成初始值
  @override
  Widget build(BuildContext context) {
    var items = List.generate(10, (index) => index);
    return  ListView.separated(itemBuilder: (context,index){
          return ListTile(
            title: Text("abc"),
            subtitle: Text("123"),
            leading: Text("456"),
            trailing: Text("789"),
            selected: selectIndex == index,
            onTap: () {
              print("index = $index");
              print("selectIndex = $selectIndex");
              setState(() {
                selectIndex = index;//设置选中的序列为当前点击的index
                print("selectIndex = $selectIndex");
              });
            },
          );
    }, separatorBuilder: (context,index){
      return Divider();
    }, itemCount: items.length);
  }
}
