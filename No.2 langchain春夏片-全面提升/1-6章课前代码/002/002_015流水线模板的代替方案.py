from langchain.prompts import PromptTemplate
#重点,最终的提示词,里面有前面所有提示词占位用的变量
# 定义第一个提示模板
prompt1 = PromptTemplate.from_template("请描述 {topic} 的主要特点。")
# 定义第二个提示模板，使用第一个模板的输出作为输入
prompt2 = PromptTemplate.from_template( "基于以下描述，给出 {topic} 的应用场景：{description}")
# 定义要处理的主题

# 渲染第一个提示模板
s1 = "人工智能"
result1 = prompt1.format(topic=s1)
print(result1)

print("第一个模板渲染结果：", result1)

# 渲染第二个提示模板
final_prompt = prompt2.format(topic=s1, description=result1)
print("最终提示结果：", final_prompt)