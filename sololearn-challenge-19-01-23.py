# Question 1
x = "9"
x = x + "0"
y = int(x) + 5
print(float(y))

# Question 2
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
print(fact(3))

# Question 3
numbers = [0, 1, 4, 8, 6]
digits = numbers
print(digits)
digits[3] = 9
print(numbers)

# Question 5
count = 0
while(count < 5):
    print(count)
    if (count > 1):
        count += 1
        break
    else:
        count +=1