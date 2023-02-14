city = ["東京", "名古屋", "大阪", "京都"]
sale = [80, 60, 22, 50, 75]

print("都市名稱資料為:", city, ".")
print("銷售額資料為:", sale, ".")

print("將資料打包.")

# zip -- pack two list
for d in zip(city, sale):
    print(d)
 
print("資料和索引值的打包.")

# enumerate -- pack with index and data
for d in enumerate(city):
    print(d)

print("將資料解包.")

# unpack the data in zip function
for c, s in zip(city, sale):
    print("都市名稱為:", c, "的銷售額為:", s)

# generate new list from exist list (List Comprehension)
data_y = [1, 2, 3, 4, 5]
print("現在的資料為:", data_y, ".")

# [Expression for val in str if abx condition is True]
ndata = [n*2 for n in data_y if n!=3]
print("新的資料為:" , ndata, ".")