import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
    runApp(MaterialApp(home:  Scaffold(
    appBar: AppBar(
    title: Text('Expanded和Column练习'),
    ),body
  :HomePage()

  )));
}
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,//宽度改成最大,可以让列的宽度跟屏幕一样大
      color: Colors.green,
      child: Column(

          mainAxisAlignment: MainAxisAlignment.end,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
          Row(
            children: [
              Spacer(),
              Container(
              // width: double.infinity,//第一个元素的宽度改成最大,这样外面的column也变成最大
              width: 100,
              height: 100,
              color: Colors.yellow,
                      ),
              Spacer(),
            ],
          ),
            Expanded(child: Container(
              color: Colors.pink,
              child: Row(
                // crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Container(
                    height: 50,
                    width: 50,
                  color: Colors.red,
                            ),
                  Container(
                    height: 50,
                    width: 50,
                    color: Colors.yellow,
                  ),
                  Container(
                    height: 50,
                    width: 50,
                    color: Colors.black,
                  ),
                ],
              ),
            ),
        ),
            Expanded(
              flex: 2,
              child: Container(
              height: 50,
              width: 80,
              color: Colors.blue,
                child: Text("abc",style: TextStyle(fontSize: 40),),
            ),
            )
      ]),
    );
  }
}
