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
  bool? isChecked = false;

  //填充颜色
  Color getColor(Set<WidgetState> states) {
    const Set<WidgetState> interactiveStates = <WidgetState>{
      WidgetState.pressed,
      WidgetState.hovered,
      WidgetState.focused,
    };
    if (states.any(interactiveStates.contains)) {
      return Colors.blue;
    }
    return Colors.orange; //修改填充颜色
  }

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      Checkbox(
        fillColor: WidgetStateProperty.resolveWith(getColor),//填充颜色
          checkColor:Colors.blueAccent,//打钩选中颜色
        // isError: true,//红框
          tristate: true,//tristate = true以后 点击 变成横线
          value: isChecked, onChanged: (value){
            print("value = $value");
            setState(() {
              isChecked = value; //注意不要给 ! ,tristate = true以后 点击 变成横线,value = null 强制解包 有null值
            });

      })
    ],);
  }
}

