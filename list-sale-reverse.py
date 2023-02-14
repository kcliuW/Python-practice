data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("現在的資料為: ", data, ".")

# data[::-1]
print("data[::-1] 在 for 敘述中進行處理.")
for d in data[::-1]:
    print(d,"\t",end ="")
print("\n","data[::-1]為:", data[::-1], ".")
print("現在的資料為: ", data, ".")

# reversed(data)
print("reversed(data) 在 for 敘述中進行處理.")
for d in reversed(data):
    print(d,"\t",end ="")

print("\n","reversed(data)為:", reversed(data), ".")
print("現在的資料為: ", data, ".")

# data.reverse()
print("data.reverse()的執行處理.")
data.reverse()
print("現在的資料為: ", data, ".")
