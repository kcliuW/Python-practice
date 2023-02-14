class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

a = Car(color="blue", mileage=20_000)
b = Car(color="red", mileage=30_000) 

for car in (a,b):
    print(f"The {car.color} car has {car.mileage} miles.")
    



    