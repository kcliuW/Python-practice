sale1 = [1, 2, 3, 4, 5, 6]
print("上半年的資料 :", sale1, ".")

sale2 = [7, 8, 9, 10, 11, 12]
print("下半年的資料 :", sale2, ".")

ysale = sale1 + sale2

print("一整年的資料為:", ysale, ".")

print(ysale[0:6])

print(ysale[6:])

print(ysale[::2])

print(ysale[::-1])

print(ysale[:-1:1])

print(ysale[:-2:1])

print(ysale[:-3:1])

ysale.reverse()

print(ysale)

sale1.extend(sale2)

print(sale1)