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

#
#
#
# Pydantic 会在数据不符合预期时抛出 ValidationError，帮助开发者提前发现和解决数据格式问题。

from langchain_openai import OpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field,field_validator
import json


# 定义 Pydantic 模型,必须是BaseModel子类
class ZhouZhou(BaseModel):
    #Field 是 Pydantic 提供的一个函数，用于对字段进行额外的配置。
    # 这里使用了 description 参数，它是一个可选参数，
    # 用于为字段添加描述信息。这个描述信息本身并不会影响数据的验
    # 证和处理，但在生成文档或调试时非常有用，可以帮助开发者
    # 更好地理解每个字段的含义。
    #定义2个类属性
    name:str = Field(min_length=2, max_length=7) #这里面定义哪个Field()就解析哪个
    age:int = Field(gt=0,le=200) #自动类型转换,自动转换为int类型
    #数字的限制ge: greater than or equal
    #lt less than 小于
    #le less than or equal 小于等于
    # name: str = Field(description="姓名")
    # age: int = Field(description="年龄")
    @field_validator("name")#这个装饰器会主动检查这个字段,后面函数名随便起
    def fieldName(cls, field):
        if "夏尼" in field :#in的左边是字符串,右边是要被查找的字符串
            print("发现错误")
            raise ValueError("发现相声界的评论家")#作用主动抛出异常,加上里面的字符串

    @field_validator("age")  # 这个装饰器会主动检查这个字段,后面函数名随便起
    def fieldAge(cls, field):
        if(field ==888):
            print("发现藏马")
ZhouZhou.age = "123"
print(type(ZhouZhou.age))
print(id(ZhouZhou.age))
ZhouZhou.age = 99 #类属性修改了值,他的地址也会变
print(type(ZhouZhou.age))
print(id(ZhouZhou.age))
print(id(789))#注意看,这里打印id地址789和ZhouZhou.age地址是相同的
ZhouZhou.name = "张三"


# 假设下面是llm大语言模型invoken之后返回的内容
result_content = '{"name": "夏尼 麻掺和12", "age": 18,"money":9999}'
print(result_content)
# 创建输出解析器
parser = PydanticOutputParser(pydantic_object=ZhouZhou)
try:
    # parse()方法的作用使用解析器解析输出
    """Parse the output of an LLM call to a pydantic object.
        解析pydantic对象的LLM调用的输出。
    Args:
        text: The output of the LLM call.
    text: LLM调用的输出。
    Returns:
        The parsed pydantic object.
        解析后的pydantic对象。
    """

    parsed = parser.parse(result_content)
    print("parsed_output=", parsed)
    # 将解析后的 Pydantic 对象转换为字典 ,dump这里是转储的意思
    #下面是V2版本中先把模型转字典->再转json,也可以直接转json
    # output_dict = parsed_output.model_dump()  #在 Pydantic V2 中，model_dump() 是替代 dict() 的官方推荐方法，用于将 Pydantic 模型实例转换为字典
    # print("转换为字典是:output_dict = ",output_dict)
    # # 将字典转换为 JSON 字符串
    # json_output = json.dumps(output_dict, ensure_ascii=False, indent=2)
    json_output = parsed.model_dump_json()
    print(json_output)
except Exception as e:
    #这里是捕获到异常以后进入这里
    print("数据验证出现以下错误：")
    print(e)

