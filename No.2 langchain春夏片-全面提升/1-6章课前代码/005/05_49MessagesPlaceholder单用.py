from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate

# MessagesPlaceholder :
# variable_name用作消息的变量名。
# optional：如果为 True，format_messages可以在不传入参数的情况下调用，并且会返回一个空列表。如果为 False，那么必须传入一个名为variable_name的命名参数，即使其值为空列表。默认值为 False。
prompt = MessagesPlaceholder(variable_name="havaspeedsystem",optional = False)
#使用方法把variable_name 变量 ,赋值给一个 list
result = prompt.format_messages(havaspeedsystem =[
    HumanMessage(content="蛋清加速系统")
])#报错,MessagesPlaceholder传入的值,必须是BaseMessage 的[]list 列表

prompt = MessagesPlaceholder(variable_name="havaspeedsystem",optional = False)#默认是否可空optional是False,是不可空
#使用方法把variable_name 变量 ,赋值给一个 list
# result = prompt.format_messages()#optional = False报错,不能是可空的,这里不能不填写havaspeedsystem
prompt2 = MessagesPlaceholder(variable_name="havaspeedsystem",optional = True)
prompt2.format_messages()#这里可以不填写havaspeedsystem ,因为optional = True

# result = prompt.invoke({"havaspeedsystem":"蛋清加速系统"})#报错:MessagesPlaceholder 对象没有 invoke 方法。这是因为 MessagesPlaceholder 主要用于在提示模板中占位，它本身不具备像 ChatPromptTemplate 那样直接调用的 invoke 方法。

print(result)
