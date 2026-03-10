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
  bool? isChecked = true; //设置默认未选中
  //填充颜色
  Color getColor(Set<MaterialState> states) {
    const Set<MaterialState> interactiveStates = <MaterialState>{
      MaterialState.pressed,
      MaterialState.hovered,
      MaterialState.focused,
    };
    if (states.any(interactiveStates.contains)) {
      return Colors.blue;
    }
    return Colors.orange; //修改填充颜色
  }
  @override
  Widget build(BuildContext context) {
    return Center(

        child: Column(children: [

          Checkbox(
            tristate: true,
            checkColor: Colors.green, //选中颜色,打钩的颜色
            value: isChecked, //value是true是设置选中,false是未选中 横线是null
            fillColor: MaterialStateProperty.resolveWith(getColor),
            onChanged: (
                bool? value) { //状态改变调用,每次点击调用状态会改变,把改变的状态赋值给 isCheck保存,并且刷新页面
              print("value = $value");
              setState(() {
                isChecked = value;
              });
            },
          ),


          Checkbox(
            tristate: true,
            value: isChecked,
            isError: true, //变成红框
            onChanged: (bool? value) {
              print("value = $value");
              setState(() {
                isChecked =
                    value; //注意不要给 ! ,tristate = true以后 点击 变成横线,value = null 强制解包应为 有null值
              });
            },
          )
          ,
        ]
        )

    );
  }
}
