import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text('标题栏'),
          ),
          body:  HomePage())));
}
class HomePage extends StatelessWidget {
   HomePage({super.key});
  // var items = [1,2,3,4];
   var items = [];
  @override
  Widget build(BuildContext context) {
    return items.length > 0
        ? ListView.builder(
      itemCount: items.length,
      itemBuilder: (BuildContext context, int index) {
        return ListTile(
          title: Text('Item ${items[index]}'),
        );
      },
    )
        // : const Center(child: Text('没有元素')
    :Center(child: const CupertinoActivityIndicator());//ios模式的转菊花 Cupertino是苹果主题,库比蒂诺是苹果公司所在地位于旧金山



  }
}