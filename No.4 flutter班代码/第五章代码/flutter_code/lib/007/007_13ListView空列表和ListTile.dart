import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text('标题栏'),
          ),
          body: HomePage())));
}

class HomePage extends StatelessWidget {
  HomePage({super.key});

  var items = [];
  // var items = [1, 2, 3, 4];

  @override
  Widget build(BuildContext context) {
    return items.length > 0 ?

      ListView.builder(
        itemCount: items.length,
        itemBuilder: (context,index){
          return ListTile(
            leading: Text("老张"),
            title:Text("${items[index]}"),
            subtitle: Text("123"),
            trailing: Text("456"),
            tileColor: Colors.yellow[100],
            onTap: () {
              print("点击了${index}");
            },
          );
    }) :
    // Center(child: Text("没有更多元素"));
Center(child: const CupertinoActivityIndicator());//苹果风格的 加载器,转菊花
//ios模式的转菊花 Cupertino是苹果主题,库比蒂诺是苹果公司所在地位于旧金山
  }
}
