height = 178
print("小郭的身高: %d" % height)

print("{0} 今年 {1} 歲. ".format("王小明", 18)) # 對應引數
print("{writer} 每年賺 {money} 版稅. ".format(writer = "陳小春", money = 60000000)) # 引數名稱

print('{0:.2f}'.format(3.14159)) # 指定參數格式 -- 取小數點後 2 位

num = 1.732659
print("num = {:.3f}".format(num)) # 取小數點後 3 位

num = 1.732659
print("num = {:7.3f}".format(num)) # 數值總長度為 7 的浮點數, 且小數點後 3 位(小數點包括在總長度內)

university = "香港大學"
year = 150
print("{} 己辦校 {} 年 ".format (university, year))