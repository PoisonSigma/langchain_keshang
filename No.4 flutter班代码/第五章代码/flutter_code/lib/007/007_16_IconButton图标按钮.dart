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
    return GestureDetector(
      onTap: () {
        print("onTap点击了");
      } ,
      child: Icon(
        Icons.remove_circle,
        color: Colors.red,
      ),
    );
      /*
      Container(
      color: Colors.green,
      child: IconButton(
        icon: Icon(
          Icons.remove_circle,
          color: Colors.red,
        ), onPressed: () {
          print("点击了");
      },
      ),
    );

       */
  }
}
