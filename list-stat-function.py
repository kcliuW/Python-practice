sale = [80, 60, 22, 50, 75]
print("現在的資料為:", sale, ".")

print("資料的最大值為:", max(sale), ".")
print("資料的最小值為:", min(sale), ".")

print("資料的總和為:", sum(sale), ".")

print("資料的排序為:", sorted(sale), ".")
print("資料的反向排序為:", sorted(sale, reverse=True), ".")

sale.sort(reverse=True)