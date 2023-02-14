data1 = [1, 2, 3, 4, 5]
data2 = list(data1)

print("data1 為", data1, ".")
print("data2 為", data2, ".")

data1[0] = 10
print("變更 data1 .")

print("data1 為", data1, ".")
print("data2 為", data2, ".")
print("因為 data2 使用 list() b  ,變成一個新的串列.")

data3 = [11, 12, 13, 14, 15]
data4 = data3.copy()
print("data4 = data3.copy()method")
print(data4)

data5 = ["John", "Mary", "Amy", "Allen", "David"]
data6 = ["Peter", "Samson", "Victor", "Felix", "Joanne"]
print("use data5.extend(data6) method to join two list")
data5.extend(data6)
print(data5)

sale_a = [11, 12, 13, 14, 15]
sale_b = [16, 17, 18, 19, 20]
# sale_a.append(sale_b) # list include another list(not recommended)
# [11, 12, 13, 14, 15, [16, 17, 18, 19, 20]]
# print(sale_a)