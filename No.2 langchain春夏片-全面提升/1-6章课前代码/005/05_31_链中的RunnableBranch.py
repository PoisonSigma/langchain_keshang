from langchain.schema.runnable import RunnableBranch, RunnableLambda

# 定义条件判断函数
def is_short(text: str) -> bool:
    return len(text) <= 10

# 定义分支处理逻辑
short_chain = RunnableLambda(lambda text: "短链"+text)
long_chain5 = RunnableLambda(lambda text: "长链5"+text)
long_chain10 = RunnableLambda(lambda text: "长链10"+text)
default_chain = RunnableLambda(lambda text: text)

# 创建分支路由,要穿参数是元组
branch = RunnableBranch(
    (is_short, short_chain),   # 条件1 → 短文本处理
    (lambda text: len(text)>5, long_chain5),  # 条件2 → 长文本处理
(lambda text: len(text)>10, long_chain10),  # 条件3→ 长文本处理 ,这里不会运行,因为>5的先执行
    default_chain              # 默认处理
)
branch2 = RunnableBranch(
    (is_short, short_chain),   # 条件1 → 短文本处理
    (lambda text: len(text)>5, long_chain5), # 条件2 → 长文本处理],  # 条件3→ 长文本处理 ,这里不会运行,因为>5的先执行
    default_chain              # 默认处理
)


# RunnableBranch 按照你定义分支的先后顺序，依次评估每个分支的条件函数。一旦某个条件函数返回 True，就会执行与之对应的可运行对象，并且不会再去评估后续的分支条件。
# 测试运行
print(branch.invoke("hi"))      # 输出: HI
print(branch.invoke("hello world"))  # 输出: hello world
print(branch.invoke("medium text55"))  # 输出: medium text