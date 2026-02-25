store = {}
store["001"] = "今年多大了?"
print("id=", store["001"])
store["001"] = "有男朋友?"
print("id=", store["001"])
store["002"] = "兄弟,把你的手机给我"
print("id002=", store["002"])
store["002"] = "这是你的备用金"
print("id002=", store["002"])
print("store=", store)
if "001" in store:
    print("找到key = 001")
if "002" in store:
    print("找到key = 002")
if "003" in store:
    print("找到key = 003")