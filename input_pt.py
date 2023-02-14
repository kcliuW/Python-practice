Chinese = int(input("Please input your chinese score:  "))
print(Chinese)

Mathematics = int(input("Please input your maths score:  "))
print(Mathematics)

English = int(input("Please enter your english score:  "))
print (English)

Total = Chinese + Mathematics + English

print("Your total score is :" + str(Total))

wages = int(input("Please enter your monthly wages:  "))
bonus = int(input("Please enter your yearly bonus:  "))
overtime = int(input("Please enter the amount of overtime payment: "))

realwage = wages + bonus + overtime

print("The total monthly wage payment is:  " + str(realwage))