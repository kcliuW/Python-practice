
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)


# A function that sort a list of dictionaries based on the "year" value of the dictionaries:'
def NewFunc(g):
    return g['year']

cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car':'VW', 'year': 2011}
]

cars.sort(key=NewFunc)
print(cars)

# A function that sort the list by the "length" of the values and "reversed":
def ufunc(k):
  return len(k)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)