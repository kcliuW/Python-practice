i = 1
def new_func():
    n = int(input("Please input the end term: "))
    return n

n = new_func()
while i <= n:
    print("*"*i)
    i = i + 1