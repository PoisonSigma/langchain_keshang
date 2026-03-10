/*
Icon不能点击,.但是IconButton 的 onPress可以点击
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
class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return IconButton(onPressed: (){
      print("点击图标");
    }, icon: const Icon(Icons.remove_circle));
  }
}

