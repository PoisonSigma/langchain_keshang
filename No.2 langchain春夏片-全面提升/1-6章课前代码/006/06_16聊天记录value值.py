import  sqlite3
import msgpack  # 替换pickle，用msgpack解析
# 连接到 SQLite 数据库
conn = sqlite3.connect("langgraph.db",check_same_thread=False)#创建链接,关闭检查相同线程,langgraph是多线程,默认sqlite是单线程
conn.row_factory = sqlite3.Row  # 这个作用是可以 record["username"],让记录的元组通过字符串作为下标访问,这个要放在创建游标之前,这样下面的记录可以按照字符串访问
#打开游标
cursor = conn.cursor()
cursor.execute("SELECT * FROM writes")
result = cursor.fetchall()
for row in result:
    print(f"thread_id: {row["thread_id"]}")
    print(f"checkpoint_ns: {row["checkpoint_ns"]}")
    print(f"checkpoint_id: {row["checkpoint_id"]}")
    print(f"task_id: {row["task_id"]}")
    print(f"idx: {row["idx"]}")
    print(f"channel: {row["channel"]}")
    print(f"type: {row["type"]}")
    # print(f"value: {row["value"]}")
    value =  row["value"]
    print("value=",value)
    unpacked_data = msgpack.unpackb(value, raw=False, use_list=False)


    print(unpacked_data)
    print("反序列化value=",unpacked_data)

#先关闭游标,再关闭连接
cursor.close()
conn.close()


