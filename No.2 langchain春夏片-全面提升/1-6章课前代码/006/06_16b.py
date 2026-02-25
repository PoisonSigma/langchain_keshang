import sqlite3
import msgpack
import re



# 连接到 SQLite 数据库
conn = sqlite3.connect("langgraph.db", check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM writes")
    result = cursor.fetchall()
    for idx, row in enumerate(result):
        print(f"===== 第 {idx + 1} 行数据 =====")
        print(f"type: {row['type']}")
        value = row["value"]
        print(f"value 二进制长度: {len(value)}")

        # 跳过空值
        if len(value) == 0:
            print("⚠️ value 为空，跳过解析\n")
            continue

        try:
            # 解析msgpack（兼容ExtType）
            unpacked_data = msgpack.unpackb(value, raw=False, use_list=False, strict_map_key=False)
            print("msgpack.unpackb = ",unpacked_data)
            content = ""

            #类型是元组tuple
            print("类型是:",type(unpacked_data))
            if isinstance(unpacked_data, (tuple, list)) and len(unpacked_data) > 0:
                ext_data = unpacked_data[0]#元组第一个元素是ExtType
                print("ext_data = ",ext_data)#ExtType 是 msgpack 协议中的「扩展类型（Extended Type）」
                # ExtType(code=5,
                        #data=b'\x94\xbdlangchain_core.messages.human\xacHumanMessage\x86\xa7content\xd9c\xe4\xbd\xa0\xe5\xa5\xbd,\xe6\x88\x91\xe6\x98\xaf\xe4\xb8\x9c\xe5\x8c\x97\xe5\x9c\x9f\xe9\xb3\x96,\xe6\x83\xb3\xe8\xa6\x81\xe5\x81\x87\xe8\xa3\x85\xe4\xbb\x8e\xe4\xbc\xa6\xe6\x95\xa6\xe5\x9b\x9e\xe6\x9d\xa5\xe7\x9a\x84,\xe4\xb8\x80\xe5\x98\xb4\xe4\xbc\xa6\xe6\x95\xa6\xe8\x85\x94,\xe8\xaf\xb7\xe9\x97\xae,\xe8\xaf\xb4\xe4\xbd\xa0\xe5\xa5\xbd\xe6\x80\x8e\xe4\xb9\x88\xe8\xaf\xb4?\xb1additional_kwargs\x80\xb1response_metadata\x80\xa4type\xa5human\xa4name\xc0\xa2id\xd9$46fee36a-5e9d-4685-9586-3cbd97d3ac83\xb3model_validate_json')
                # 提取ExtType的data字段（二进制）
                if hasattr(ext_data, 'data'):
                    # 直接从二进制提取中文（避免解码错误）
                    # 直接匹配二进制中的UTF8中文字节模式，再解码
                    chinese_bytes = re.findall(b'[\xe4-\xe9][\x80-\xbf][\x80-\xbf]+', ext_data.data)
                    # 拼接后解码为UTF8字符串
                    text = ''.join([b.decode('utf-8', errors='ignore') for b in chinese_bytes])
                    content =  text

            print(f"✅ 解析后的核心内容：{content}")

        except Exception as e:
            print(f"❌ 解析失败：{type(e).__name__} - {e}")
            # 应急提取：直接从value二进制中提取中文

            

except Exception as e:
    print(f"程序整体错误：{e}")
finally:
    cursor.close()
    conn.close()