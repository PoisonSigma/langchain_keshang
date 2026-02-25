import sqlite3


# 连接到 SQLite 数据库
conn = sqlite3.connect("langgraph.db", check_same_thread=False)
conn.row_factory = sqlite3.Row  # 这个作用是可以 record["username"],让记录的元组通过字符串作为下标访问,这个要放在创建游标之前,这样下面的记录可以按照字符串访问
cursor = conn.cursor()
# 第一步：查看数据库中的表结构（验证字段）
print("=== 数据库表结构 ===")
cursor.execute("SELECT * FROM writes ;")
tables = cursor.fetchall()

cursor.execute("""
    SELECT *
    FROM writes 
""")
rows = cursor.fetchall()
for row in rows:
    print("row=",row)
    print(f"thread_id: {row["thread_id"]}")
    print(f"checkpoint_ns: {row["checkpoint_ns"]}")
    print(f"checkpoint_id: {row["checkpoint_id"]}")
    print(f"task_id: {row["task_id"]}")
    print(f"idx: {row["idx"]}")
    print(f"channel: {row["channel"]}")
    print(f"type: {row["type"]}")
    print(f"value: {row["value"]}")

# 关闭连接
cursor.close()
conn.close()