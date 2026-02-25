from langchain_core.prompts import load_prompt, PromptTemplate
#load_prompt 读取模板,里面带文件路径
t1 =  load_prompt("../assets/002_017.yaml")
print(t1)
p1 = t1.format(cartoon="jojo的奇妙冒险",name="吉良吉影")
print(p1)