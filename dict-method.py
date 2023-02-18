# clear method
dic = {'name': '網路行銷', 'author': '許志峰', 'publisher': '先進出版社'}
dic.clear()
print(dic)

# copy method
dic1 = {"title":"行動行銷", "year":2018, "author":"陳來貴"}
dic2 = dic1.copy()
print(dic2) # 新複製的字典和 dic1 內容一致
dic2["title"]="網路概論" # 修改新字典 dic2 的內容
print(dic2) # 新字典內容已和原字典 dic1 內容不一致
print(dic1) # 原字典內容不會受到新字典 dic2 內容而更改內容

# get method
dic1 = {"title":"行動行銷", "year":2018, "author":"陳來貴"}
owner = dic1.get('author')
print(owner) # 輸出 "陳來貴"
owner = dic1.get('color')
print(owner) # 印出 None
owner = dic1.get('color','白色封面')
print(owner) # 印出 '白色封面'

# pop method
dic1 = {"title":"行動行銷", "year":2018, "author":"陳來貴"}
dic1.pop('title')
print(dic1) # 印出 {"year":2018, "author":"陳來貴"}