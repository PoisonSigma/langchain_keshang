import sqlite3
# 验证数据库是否可正常读取
def check_sqlite_db(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # 查询表结构（LangGraph生成的核心表）
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("数据库中的表：", tables)
        # 读取checkpoints表数据（验证数据是否存在）
        cursor.execute("SELECT * FROM checkpoints LIMIT 1;")
        checkpoint_data = cursor.fetchone()
        print("Checkpoints表第一条数据：", checkpoint_data)
        conn.close()
        print("数据库验证正常，文件结构完整")
    except Exception as e:
        print("数据库损坏：", e)

check_sqlite_db("langgraph.db")