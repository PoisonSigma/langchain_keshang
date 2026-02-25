
from test2 import invoke,stream
print(invoke("你好"))
for item in stream():
    print(item)
# import test2
# test2.invoke("add",1,2)
# test2.stream("add",1,2)