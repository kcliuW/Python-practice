# Example 1
total = 0
for count in range(1,101):
    total += count
print("數字 1 累加到 100 的總和 = ", total)

# Example 2
total = 0
for count in range(1,100,2):
    total += count
print("數字 1 累加到 100 的奇數總和 = ", total)

# Example 3 (enumerate)
phrase = ["三陽啟泰", "事事如意", "五福臨門"]
for index, x in enumerate(phrase):
    print("{0}--{1}".format(index, x))

