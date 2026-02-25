from langchain.prompts import example_selector
from langchain_core.example_selectors import BaseExampleSelector, LengthBasedExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

examples:list[dict[str:str]]= [
    {"i": "橘子", "o": "水果"},
    {"i": "香蕉", "o": "水果"},
    {"i": "西瓜", "o": "水果"},
    {"i": "黄瓜", "o": "蔬菜"},
    {"i": "豆角", "o": "蔬菜"},
]
example_prompt = PromptTemplate.from_template("你输入了一个{i}给出的输出是{o}")
# examples= [
# example_selector: Optional[BaseExampleSelector] = None
#cmd+左键点击这个类,会看到所有用到这个类的地方,找到class LengthBasedExampleSelector(BaseExampleSelector, BaseModel):
example_selector = LengthBasedExampleSelector(
    examples=examples,
 # examples= [{True:False}],
# examples= None,
    example_prompt = example_prompt,
    max_length= 5,
)
# print(example_selector)
fspt = FewShotPromptTemplate(
example_prompt = example_prompt,
    example_selector = example_selector,
    # 前缀prefix
    prefix="请根据我提供的下列例子,进行推理",
    # 后缀,suffix 放在整个提示词模板的结尾
    suffix="请告诉我{name}对应的推理出来的词是什么"
)
msg = fspt.format(name = '西红柿')
print(msg)