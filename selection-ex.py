a = int(input("Please enter the number: "))
selection = input("Please choose your selection (1 or 2): ")

if selection == '1':
    answer = a * a # 計算 a 的平方值指定給變數 answer
    print("平方值為 : %d" %answer)

if selection == '2':
    answer = a * a * a # 計算 a 的立方值指定給變數 answer
    print("立方值為 : %d" %answer)
