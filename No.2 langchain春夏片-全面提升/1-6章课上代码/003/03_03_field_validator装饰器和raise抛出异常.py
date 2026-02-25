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
import json

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, field_validator

#
#
#
# Pydantic 会在数据不符合预期时抛出 ValidationError，帮助开发者提前发现和解决数据格式问题。

# 假设下面是从llm返回的结果存入了result里面res.content
res_content = '{"name": "张三", "age": 18,"money":9999}'


# 定义 Pydantic 模型,必须是BaseModel子类
class ZhouZhou(BaseModel):
    # Field 是 Pydantic 提供的一个函数，用于对字段进行额外的配置。
    # 这里使用了 description 参数，它是一个可选参数，
    # 用于为字段添加描述信息。这个描述信息本身并不会影响数据的验
    # 证和处理，但在生成文档或调试时非常有用，可以帮助开发者
    # 更好地理解每个字段的含义。
    # 定义2个类属性
    # 类成员变量=Field()这样的格式去定义接受的key
    name: str = Field(min_length=2, max_length=6, description="姓名")  # 字符串长度
    age: int = Field(gt=0, lt=999, description="年龄")  # 限定一个验证的大小
    @field_validator("name")
    def name_validator(cls, value): #验证的方法结果必须返回属性,不返回就是返回None
        if "夏尼" in value:
            print("发现相声界的评论家,红色预警")
            raise ValueError("现相声界的评论家,快跑")#作用主动抛出异常,加上里面的字符串
        return value
    @field_validator("age")
    def age_validator(cls, value):
        print("value =",value)
        if value == 888:
            print("发现藏马")
            raise  ValueError("发现大帅哥,快跑,要变绿叶了")
        return value
    # 数字的限制
    # ge: greater than or equal 大于等于
    # gt :greater than 大于
    # lt less than 小于
    # le less than or equal 小于等于
    # name: str = Field(description="姓名")
    # age: int = Field(description="年龄")


# 假如下面是llm返回的最终结果
res_content = '{"name": "麻掺和", "age": 18,"money":9999}'  # 假如这个是llm传回的字符串,符合json格式
parser = PydanticOutputParser(pydantic_object=ZhouZhou)  # 传入json格式的字符串
try:
    # 这里是try要运行的代码,如果发现出错,就跳入到西面except中去
    # 如果分析器的BaseModel的子类不符合验证,就会被try捕获到
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
    parsed = parser.parse(res_content)  # 开始转换
    # print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

    print(parsed)
    dic = parsed.model_dump()  # 转字典
    # print("字典=",dic)
    # print("dic['name']=",dic["name"])#双引号里面如果再用字符串,就用单引号
    # print('dic["name"]=', dic["name"])  # 外单内双,引号,混用
    json = json.dumps(dic, ensure_ascii=False, indent=2)
    # ensure_ascii默认值是True如果是非英文的默认会转义输出,如果是False会原样输出

    # indent=2
    # 默认值：该参数的默认值为 None，当 indent 为 None 时，生成的 JSON 字符串是紧凑格式，所有内容都在一行，没有换行和缩进。
    # 设置缩进值的作用：当为 indent 参数指定一个整数时，生成的 JSON 字符串会按照指定的缩进空格数进行格式化，使其更具可读性。这里设置 indent=2 表示每个层级的缩进为 2 个空格。
    # print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
    # print(json)

    # json = parsed.model_dump_json()#先变字典再变json
    print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

    print("json=", json)
except Exception as error:
    # 这里是捕获的异常,就执行下面的代码,e是异常的变量
    print("出错了:铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
    print(error)
