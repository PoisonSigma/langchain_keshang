/*
模型工具制作gitee地址:
https://gitee.com/wx18903612715/flutter-model-making-tool
gitee地址,如果好用,请点小星星
 */

class UserItemA1 {
  String img = "";
  String userName = "";
  String isSelected = "";

  UserItemA1.fromMap(Map map){
    try {
      img = map['img'] ?? "";
      userName = map['userName'] ?? "";
      isSelected = map['isSelected'] ?? "";
    }catch(e){
      print("错误e=$e");
    }
  }
  UserItemA1({
    required this.img,
    required this.userName,
    required this.isSelected,
  });

  @override
  String toString() {
    return "img:$img,userName:$userName,isSelected:$isSelected";
  }
}