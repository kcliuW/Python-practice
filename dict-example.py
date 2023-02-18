# Example 1
dic = {'length':4, 'width':8, 'height':12}
print(dic)

# Example 2
dic = {'name': 'Python程式設計', 'author': '許志峰', 'publisher': '先進出版社'} 
print(dic['name'])
print(dic['author'])
print(dic['publisher'])

# Example 3
dic = {'name': 'Python程式設計', 'author': '許志峰', 'publisher': '先進出版社'} 
dic['name'] = '網路行銷' # 將字典中的['name']鍵的值修改為'網路行銷'
print(dic)

# Example 4
dic = {'name': '網路行銷', 'author': '許志峰', 'publisher': '先進出版社'}
dic['price'] = 580
print(dic)

dic ={'name':'Peter Anderson', 'age':18, 'nation':'英國', 'nation':'日本'}
print(dic['nation']) # 會印出日本

# Example 5
dic ={'name':'Peter Anderson', 'age':18, 'nation':'英國', 'nation':'日本'}
del dic['age']
print(dic)
del dic

# Example 6
english = {'春':'Spring', '夏':'Summer', '秋':'Fall', '冬':'Winter'}
# 字典內容
del english ['秋'] # 刪除字典指定鍵值的元素
print(english)
del english # 刪除整個字典
        