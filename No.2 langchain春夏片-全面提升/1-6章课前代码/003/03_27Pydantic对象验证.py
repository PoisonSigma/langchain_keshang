from pydantic import BaseModel, Field, model_validator, field_validator
class JoJo(BaseModel):

    name: str = Field(description="jojo的奇妙冒险中的一个人物名字")#放在init构造函数外面的是类属性
    age: int = Field(description="年龄")

    @field_validator("age")
    def age_fun(cls,value):
        if value < 18:
            print("未成年人不允许装13")
            # raise ValueError("未成年人不允许装13")
        if value >65:
            print("退休了,出去抽嘎吧,或者每天打游戏")
            # raise  ValueError("退休了,可以每天回家打游戏了")
        return value
JoJo(name = "张三",age = 13)#对象被创建的时候就能验证
