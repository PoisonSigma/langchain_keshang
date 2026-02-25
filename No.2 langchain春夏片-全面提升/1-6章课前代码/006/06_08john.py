docs = ["1","a","b"]
system_message = """仅使用以下提供的信息回答用户的问题：:

{docs}""".format(docs="\n".join(docs)) #docs="\n".join(docs)的作用是把后面的list迭代,然后每个后面加入 换行"\n"
print(system_message)