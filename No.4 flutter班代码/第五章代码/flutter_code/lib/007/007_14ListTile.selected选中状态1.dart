/*
ListTile.selected选中状态
ListTile 有一个 selected 参数,这个参数如果 给false,那么就是默认主题颜色, 如果是true 颜色就是选中浅色
这个默认的没选中颜色是变浅
 */
// 默认情况下，选定的颜色是主题的主要颜色。可以使用 ListTileTheme 来覆盖选定的颜色

import 'package:flutter/material.dart';

main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text('标题栏'),
          ),
          body: HomePage())));
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  var isSelected = false;

  @override
  Widget build(BuildContext context) {
    print("build执行");
    return ListTile(
      title: Text("abc"),
      subtitle: Text("abc"),
      leading: Text("abc"),
      trailing: Text("abc"),
      selected: isSelected,
      onTap: () {
        print(isSelected);
        isSelected = !isSelected;
        print(isSelected);
        setState(() {
        });
      },
    );
  }
}
