def decor(func):
    print("_ _ _ _ _ _ _ _ _ _ \n")
    func()
    print("_ _ _ _ _ _ _ _ _ _ ")

@decor
def hello_world():
    print("Hello World")

""" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"""

def hello():
    print("Hello")

decor(hello)