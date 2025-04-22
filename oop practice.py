class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        print("Hello from Child!")

obj = Child()
obj.greet()  # This will call the greet method from the Child class