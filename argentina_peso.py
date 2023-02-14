peso = int(input("Please enter the amount of Peso: "))
dollar = int(input("Please enter the amount of dollars: "))

if peso * 0.02 > dollar:
    print('Dollars')

else:
    print('Pesos')