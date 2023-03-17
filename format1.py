print("{0} 駕照考了 {1}次.".format("陳美鳳", 5))

print("{person} 一年收入新台幣 {money} 元".format(person = "許富強", money = 1000000))

print('{0:.3}'.format(1.732))

company = "藍海科技股份有限公司"
year = 30
print("{} 已經成立了 {} 年".format (company, year))

str = "{1} * {0} = {2}"
a = 3
b = "5"
print(str.format(a,b, a * int(b)))

print("{0:10} 收入: {1:_^12}".format("Axel", 52000))
print("{0:10} 收入: {1:>12}".format("Michael", 87000))
print("{0:10} 收入: {1:*<12}".format("May", 36000))

print("------------------------------------------------")

print("編號 姓名   底薪 業務獎金 加給補貼")
print("%3d %3s %6d %6d %6d" %(801,"朱元璋",32000,10000,5000))
print("%3d %3s %6d %6d %6d" %(805,"曾國藩",35000,8000,7000))
print("%3d %3s %6d %6d %6d" %(811,"陳近南",32000,10000,5000))