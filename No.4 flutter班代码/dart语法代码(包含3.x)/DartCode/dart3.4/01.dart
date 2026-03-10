// import 'package:json/json.dart';
@JsonCodable()
class Vehicle {
  final String description;
  final int wheels;
  Vehicle(this.description, this.wheels);
}
void main() {
  final jsonString = Vehicle('bicycle', 2).toJson();
  print('Vehicle serialized: $jsonString');
}
