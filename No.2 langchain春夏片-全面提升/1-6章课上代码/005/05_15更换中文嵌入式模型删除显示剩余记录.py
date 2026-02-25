from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from torch.utils.hipify.hipify_python import meta_data


list1 = [
    "李阿姨说:这不是西格玛军儿吗?",
    "咋不说话了呢?军儿",
    "你不心中无女人,拔刀自然神吗?",
    "军儿说话啊?",
    "军说:我错了李阿姨?以后不敢装了,之前是我年少不知阿姨好,老了发现阿姨是块宝",
    "面试的时候应该注意什么",
    "如何与同事进行有效的沟通",
    "怎样提高工作效率",
    "职场晋升需要具备哪些能力",
    ]
print(len(list1))
docs = []
for i in range(len(list1)):
    # print(list1[i])
    str1 = "语录"+str(i)
    # print(str1)
    docs.append(Document(page_content=list1[i],metadata = {"李阿姨的复仇":str1},id = str(i)))
# print(docs)
# vector_store = InMemoryVectorStore.from_documents(docs,HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))

# ~/.cache/huggingface/hub
#HuggingFaceEmbeddings 是langchain的一个包 ,model_name才是模型
vector_store = InMemoryVectorStore(HuggingFaceEmbeddings(model_name="shibing624/text2vec-base-chinese"))
vector_store.add_documents(docs) #添加记录
result = vector_store.similarity_search("工作",k =2 )#相似性搜索,k是搜索显示的最大记录,默认是4
for i in range(len(result)):
    print("第",i,"条记录:", result[i])
    print(type(result[i]))
print(len(vector_store.store))#这个是剩余的个数
vector_store.delete(ids=[ '0'])#根据id删除
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

for i in vector_store.store.keys():
    print(vector_store.store[i]['id'])
    print(vector_store.store[i]['vector'])
    print(vector_store.store[i]["text"])
    print(vector_store.store[i]["metadata"])

dic1 =  {"name":"张三","age":18}
print(len(dic1))#len可以取到字典里面的键值对的个数
print(dic1.keys())
for key in dic1.keys():
    print(dic1[key])

print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
#搜索条件为""空字符串,但是搜索最大个数,取最大记录数
result = vector_store.similarity_search("",len(vector_store.store))
for i in range(len(result)):
    print(result[i].page_content)




