a = float(input("Please input a number: "))
b = float(input("Please input a number: "))
op_key = input("Please input +, -, *, / key: ")
if op_key == "+":
    print("{} {} {} = {}".format(a, op_key, b, a + b))

elif op_key == "-":
    print("{} {} {} = {}".format(a, op_key, b, a - b))

elif op_key == "*":
    print("{} {} {} = {}".format(a, op_key, b, a * b))

elif op_key == "/":
    print("{} {} {} = {}".format(a, op_key, b, a / b))

else:
    print("Wrong operation key! ")