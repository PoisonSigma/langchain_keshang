import 'package:flutter/material.dart';
main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text('标题栏'),
          ),
          body:  HomePage())));
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  var items = List.generate(10, (index) => index);
  var selectedIndex = -1;//设置选中的序列,注意这个不用放在build里面,否则每次刷新页面,他都变成初始值
  @override
  Widget build(BuildContext context) {

    print("selectedIndex = $selectedIndex");
    return  ListView.separated(itemBuilder: (context,  index){
      return ListTile(
        title: Text("${items[index]}"),
        subtitle: Text("${items[index]}"),
        leading: Text("${items[index]}"),
        trailing: Text("${items[index]}"),
        selected: selectedIndex == index,
        onTap: () {
          print("index=$index");
          selectedIndex = index;
          print("selectedIndex = $selectedIndex");
          setState(() {
          });
        },
      );


    }, separatorBuilder: (context,index){
      return Divider();
    }, itemCount: items.length);
  }
}

