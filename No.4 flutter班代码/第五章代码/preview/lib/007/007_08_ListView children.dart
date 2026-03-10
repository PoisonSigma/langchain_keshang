/*
ListView
 */
import 'package:flutter/material.dart';

main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text('标题栏'),
          ),
          body: const HomePage())));
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.green,
      child: ListView(
//默认的是使用children 列表 ,里面给子元素
        children: [
          Text(
            "1111",
            style: TextStyle(fontSize: 44),
          ),
          Text(
            "1111",
            style: TextStyle(fontSize: 44),
          ),
          Text(
            "1111",
            style: TextStyle(fontSize: 44),
          ),
          Text(
            "1111",
            style: TextStyle(fontSize: 44),
          ),
        ],
      ),
    );
  }
}
