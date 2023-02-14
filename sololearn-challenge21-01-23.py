# Question 1
num1, num2 = 3, 3
num1 -= 3
num2 = -3
print(num1 + num2)

# Question 2
import re
msg = "get, wet, set, Net"
all_msg = re.findall("[gwsn]et", msg)
print(len(all_msg)) 

# Question 3
a =[0, 1, 2]
b =[0, 1, 2]
print(a is b)

# Question 4
n = [1, 2, 3, 4]
o = list(filter(lambda x: x > 2, n))
print(o)
print(o[1])

# Question 5
try:
    print(True/False)
except:
    print("error")