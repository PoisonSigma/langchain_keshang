# 场景	json.loads 无法验证,访问是字符串加key访问例如 json["age"],需要手动转换类型int("18")验证
#
# Pydantic
# json转模型,可以进行对象名.成员变量,例如 obj.name,可以验证错误
# Pydantic 是一个基于 Python 类型提示的数据验证和设置管理库，
# 用于确保数据格式的正确性和一致性。
# 它通过定义数据模型（如继承自 BaseModel 的类）来自动验证和解析输入数据，
# 并提供类型转换、错误处理等功能。
# 发音
# Pydantic 的发音为：
# /paɪˈdæn.tɪk/（谐音：派 - 丹 - 提克）
# 重音在第二个音节 "dan"。
# 示例
# 使用 Pydantic 定义一个数据模型：
from pydantic import BaseModel, Field

#
#
#
# Pydantic 会在数据不符合预期时抛出 ValidationError，帮助开发者提前发现和解决数据格式问题。

#假设下面是从llm返回的结果存入了result里面res.content
res_content = '{"name": "张三", "age": 18,"money":9999}'

# 定义 Pydantic 模型,必须是BaseModel子类
class ZhouZhou:
    gender:str
    def __init__(self,age = 18,name = "",money = 9999):
        # self.age = 18
        # self.name = "刘华强"
        self.age:int= 0
        self.name:str = ""
ZhouZhou.gender = "男"
ZhouZhou.gender = "女"
p3 = ZhouZhou()
p3.gender = "abc"
ZhouZhou().gender= "456"
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

print(ZhouZhou.gender)
print(ZhouZhou().gender)
print(p3.gender)
p1 = ZhouZhou()
p1.age = 18
p2  = ZhouZhou()
p2.age = 18

print(id(p1.age))
print(id(p2.age))

ZhouZhou().name = "你活爹"
ZhouZhou().age = 200000