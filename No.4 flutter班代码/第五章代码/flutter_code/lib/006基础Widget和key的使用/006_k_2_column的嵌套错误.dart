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
    return Column(
      children: <Widget>[
        // Container(
        //   height: 2000,
        //   width: 2000,
        //   color: Colors.yellow,
        // ),
        Container(
          height: 800,
          child: Column(
            mainAxisSize: MainAxisSize.max,
            children: <Widget>[
              Expanded(
                flex: 1,
                child:
              Container(
                  color: Colors.red,
                ),
              )

            ],
          ),
        ),
      ],
    );
  }
}