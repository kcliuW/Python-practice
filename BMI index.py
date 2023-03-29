# 1) BMI formula : weight / (height)**2

print("Hello! Welcome to BMI calculator:")

weight = float(input("Please enter your weight(kg):"))
height = float(input("Please enter your height(m):"))

BMI = weight / (height**2)

print("This is your BMI value: ",round(BMI,2))
print("Thank you for using this program.")

# 2) Condition
if BMI < 18.5:
    print("Your weight is too low! Please consume more!")
    
elif 18.5 <= BMI < 24:
    print("Well done! You are healthy, keep on.")

else:
    print("This is abnormal! Do more exercise!")