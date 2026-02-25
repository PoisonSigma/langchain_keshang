from typing import Any

from pydantic import BaseModel, Field, field_validator
class ZhouZhou(BaseModel):
    name: str = Field(description="jojo的奇妙冒险中的一个人物名字")
    age:int = Field(description="年龄")
    @field_validator('age')
    def validate_age(cls,value):
        if value < 18:
            print("未满十八岁")
            # raise ValueError("西格玛男人,从不落入女人陷阱")
        if value > 65:
            print("退休了,可以回家打游戏,到大街上,抽嘎了")
        return value
ZhouZhou(name ="空条承太郎", age=13)#对象被创建的时候就会执行验证
ZhouZhou(name ="空条承太郎", age=66)#对象被创建的时候就会执行验证

